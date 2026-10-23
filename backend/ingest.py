"""
S2 Legal AI Pro - Complete Ingestion Pipeline
Module: backend.ingest

Parses, chunks, embeds, and stores:
1. Complete Constitution of India records (Preamble, Parts I-XXII, Articles 1-395, Schedules)
2. Landmark Supreme Court of India Judgments and Precedents (Kesavananda, Maneka Gandhi, Puttaswamy, etc.)

Embeds using BAAI/bge-small-en-v1.5 into local persistent ChromaDB storage.
"""

from __future__ import annotations

import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import List

# Ensure project root is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import chromadb

# Configure structured terminal logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("INGEST_PIPELINE")

# Directory and Model Configuration
BASE_DIR: Path = Path(__file__).resolve().parent
DATA_DIR: Path = BASE_DIR / "data"
DB_DIR: Path = BASE_DIR / "db" / "chroma_data"
COLLECTION_NAME: str = "indian_legal_corpus"
EMBEDDING_MODEL_NAME: str = "BAAI/bge-small-en-v1.5"

CHUNK_SIZE: int = 1000
CHUNK_OVERLAP: int = 200


def load_all_legal_documents(data_dir: Path) -> List[Document]:
    """
    Loads all legal corpora:
    1. The Constitution Book from backend/data/constitution/ (Original Manuscript & Authoritative Edition)
    2. Landmark Supreme Court Judgments from backend/data/supreme_court_judgments.pdf
    3. Sample Arbitration Act and Commercial Contracts from backend/data/
    Excludes any legacy synthetic constitution.pdf in backend/data/.
    """
    all_docs: List[Document] = []

    # 1. Load Constitution book from data/constitution/
    const_dir = data_dir / "constitution"
    if const_dir.exists():
        const_pdfs = sorted(list(const_dir.glob("*.pdf")))
        logger.info(f"[INGEST] Found {len(const_pdfs)} Constitution book files in {const_dir}")
        for pdf_path in const_pdfs:
            logger.info(f"[INGEST] Loading Constitution Book: {pdf_path.name}")
            try:
                loader = PyPDFLoader(str(pdf_path))
                docs = loader.load()
                valid_pages = 0
                for d in docs:
                    text = d.page_content.strip()
                    # Only include pages with meaningful legal/English content
                    # Filter out pages that are pure OCR noise (<12 words or mostly non-alphanumeric)
                    words = re.findall(r"\b[a-zA-Z]{3,}\b", text)
                    if len(words) >= 12 or "SOVEREIGN" in text or "CONSTITUTION" in text:
                        d.metadata["source_file"] = f"Constitution of India ({pdf_path.name})"
                        d.metadata["corpus"] = "constitution_book"
                        all_docs.append(d)
                        valid_pages += 1
                logger.info(
                    f"[INGEST] Loaded {valid_pages} valid statutory pages from {pdf_path.name} (out of {len(docs)} pages)"
                )
            except Exception as load_err:
                logger.warning(f"[INGEST] Notice loading {pdf_path.name}: {load_err}")

    # 2. Load other statutory corpora in data/ (Supreme Court Judgments, Arbitration, Contracts)
    top_level_pdfs = sorted(list(data_dir.glob("*.pdf")))
    for pdf_path in top_level_pdfs:
        # Exclude legacy synthetic constitution.pdf if present
        if pdf_path.name.lower() == "constitution.pdf":
            logger.info(f"[INGEST] Skipping legacy generated {pdf_path.name} per user instruction.")
            continue

        logger.info(f"[INGEST] Reading statutory document: {pdf_path.name}")
        try:
            loader = PyPDFLoader(str(pdf_path))
            docs = loader.load()
            for d in docs:
                d.metadata["source_file"] = pdf_path.name
                d.metadata["corpus"] = "statutory_precedents"
                all_docs.append(d)
            logger.info(f"[INGEST] Successfully loaded {len(docs)} pages from {pdf_path.name}")
        except Exception as top_err:
            logger.warning(f"[INGEST] Error reading {pdf_path.name}: {top_err}")

    return all_docs


def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Splits legal documents hierarchically with article and judgment boundaries preserved.
    """
    logger.info(
        f"[INGEST] Initializing RecursiveCharacterTextSplitter "
        f"(chunk_size={CHUNK_SIZE}, chunk_overlap={CHUNK_OVERLAP})..."
    )
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\nLANDMARK SC: ",
            "\n\nARTICLE ",
            "\n\nArticle ",
            "\n\nPART ",
            "\n\nPart ",
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
        is_separator_regex=False,
    )
    chunks = splitter.split_documents(documents)
    logger.info(f"[INGEST] Generated {len(chunks)} contextual chunks across all statutory corpora.")
    return chunks


def initialize_embeddings(model_name: str) -> HuggingFaceEmbeddings:
    """Initializes local CPU-optimized HuggingFace embeddings."""
    logger.info(f"[INGEST] Initializing embedding model: {model_name}...")
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    logger.info(f"[INGEST] Embedding model {model_name} ready.")
    return embeddings


def store_in_chromadb(
    chunks: List[Document],
    embeddings: HuggingFaceEmbeddings,
    db_path: Path,
    collection_name: str,
) -> Chroma:
    """Stores and indexes all document chunks in ChromaDB with cosine distance metric."""
    db_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"[INGEST] Connecting to ChromaDB storage at: {db_path}")

    client = chromadb.PersistentClient(path=str(db_path))

    # Reset collection to ensure clean update
    try:
        existing = client.get_collection(collection_name)
        if existing.count() > 0:
            logger.info(f"[INGEST] Deleting existing collection '{collection_name}' with {existing.count()} vectors...")
            client.delete_collection(collection_name)
    except Exception:
        pass

    vector_store = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embeddings,
        collection_metadata={"hnsw:space": "cosine"},
    )

    logger.info(f"[INGEST] Embedding and persisting {len(chunks)} chunks into ChromaDB...")
    start_time = time.time()

    batch_size = 64
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        vector_store.add_documents(documents=batch)
        logger.info(f"[INGEST] Indexed chunks {i + 1} to {min(i + len(batch), len(chunks))} of {len(chunks)}")

    elapsed = time.time() - start_time
    total_indexed = vector_store._collection.count()
    logger.info(
        f"[INGEST] Ingestion complete in {elapsed:.2f}s! Total persisted chunks in '{collection_name}': {total_indexed}"
    )
    return vector_store


def run_ingestion() -> None:
    print("\n" + "=" * 70)
    print("  S2 LEGAL AI PRO: COMPREHENSIVE RAG INGESTION PIPELINE")
    print("  Corpus: Indian Constitution Book (backend/data/constitution/) + Supreme Court Precedents")
    print("=" * 70 + "\n")

    try:
        # Step 0: Ensure constitution book and statutory corpora exist
        const_dir = DATA_DIR / "constitution"
        book_path = const_dir / "the_constitution_of_india_authoritative_edition.pdf"
        if not book_path.exists():
            from backend.build_constitution_book import build_constitution_book
            build_constitution_book(const_dir)

        # Remove legacy generated file if present
        legacy_path = DATA_DIR / "constitution.pdf"
        if legacy_path.exists():
            try:
                legacy_path.unlink()
                logger.info(f"[INGEST] Removed legacy generated {legacy_path.name}")
            except Exception:
                pass

        # Step 1: Load all legal documents
        documents = load_all_legal_documents(DATA_DIR)

        # Step 2: Split into contextual chunks
        chunks = chunk_documents(documents)

        # Step 3: Initialize embedding model
        embeddings = initialize_embeddings(EMBEDDING_MODEL_NAME)

        # Step 4: Persist into ChromaDB
        vector_store = store_in_chromadb(
            chunks=chunks,
            embeddings=embeddings,
            db_path=DB_DIR,
            collection_name=COLLECTION_NAME,
        )

        total_persisted = vector_store._collection.count()

        print("\n" + "=" * 70)
        print("  [RESEARCH TELEMETRY] INGESTION COMPLETED SUCCESSFULLY")
        print(f"  Total Statutory Pages Processed : {len(documents)}")
        print(f"  Total Vector Chunks Generated   : {len(chunks)}")
        print(f"  Total Chunks Persisted in DB    : {total_persisted}")
        print(f"  Target Collection Name          : {COLLECTION_NAME}")
        print(f"  Persistent Vector Store Path    : {DB_DIR}")
        print("=" * 70 + "\n")

    except Exception as exc:
        logger.error(f"[INGEST] Critical error during ingestion: {exc}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    run_ingestion()
