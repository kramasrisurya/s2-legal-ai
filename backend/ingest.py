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

# Ensure corpus builder is available
from backend.corpus_builder import generate_all_corpus_files

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
    Loads all legal corpora from PDF files in backend/data/, including
    constitution.pdf and supreme_court_judgments.pdf.
    """
    pdf_files = list(data_dir.glob("*.pdf"))
    if not pdf_files:
        logger.warning(f"[INGEST] No PDF files found in {data_dir}. Generating corpora...")
        generate_all_corpus_files(data_dir)
        pdf_files = list(data_dir.glob("*.pdf"))

    all_docs: List[Document] = []
    for pdf_path in sorted(pdf_files):
        logger.info(f"[INGEST] Reading statutory document: {pdf_path.name}")
        loader = PyPDFLoader(str(pdf_path))
        docs = loader.load()
        for d in docs:
            d.metadata["source_file"] = pdf_path.name
        all_docs.extend(docs)
        logger.info(f"[INGEST] Successfully loaded {len(docs)} pages from {pdf_path.name}")

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
    print("  Corpus: Indian Constitution (Whole) + Supreme Court Precedents")
    print("=" * 70 + "\n")

    try:
        # Step 0: Ensure corpora exist
        generate_all_corpus_files(DATA_DIR)

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
