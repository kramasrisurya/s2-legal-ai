# S2 Legal AI Pro: Router-Based Agentic RAG Architecture

A research-grade, privacy-preserving hybrid legal reasoning system designed for **Indian Jurisprudence**. Serves as the technical foundation for academic research on verifiable, privacy-compliant legal artificial intelligence.

---

## 🏛️ Key Capabilities

- **Local-First Privacy Architecture**: Resolves confidential constitutional and precedent inquiries completely on-device via ChromaDB and local LLM inference (Ollama / Llama 3 / Mistral), ensuring complete data confidentiality and compliance with lawyer-client privilege.
- **Calibrated Semantic Router ($\tau = 0.75$)**: Uses normalized sentence embeddings (`BAAI/bge-small-en-v1.5`) with domain lexical corroboration to route queries dynamically:
  - **In-Domain ($\ge 0.75$)**: Local Constitutional RAG with explicit Article/precedent citations and green trust badge.
  - **Out-of-Domain ($< 0.75$)**: Real-time grounded online search (Gemini 2.5 Flash / DuckDuckGo / Wikipedia) covering substantive penal codes (BNS 2023, BNSS 2023, BSA 2023, IPC, CrPC) and statutory concordance.
- **Trust & Verification Badges**: Transparent inference lineage with collapsible citation drawers and similarity score badges.
- **Complete Indian Legal Corpus**:
  - Entire Constitution of India (Preamble, Parts I–XXII, Articles 1–395, Schedules).
  - 16 Landmark Supreme Court of India Precedents (*Kesavananda Bharati*, *Maneka Gandhi*, *K.S. Puttaswamy*, *Satender Kumar Antil*, *Arnesh Kumar*, *Lalita Kumari*, *D.K. Basu*, *Shreya Singhal*, *Navtej Singh Johar*, *Joseph Shine*, *Vishaka*, *Indra Sawhney*, *S.R. Bommai*, *Shayara Bano*, *Common Cause*, *ADR v. Union of India*).

---

## 🛠️ Architecture Overview

```
                        [ User Query ]
                              │
               ┌──────────────┴──────────────┐
     Conversational?                         Legal Query
     ("hi, who are you")                          │
               │                            Local ChromaDB
    Architecture Overview              (BAAI/bge-small-en-v1.5)
               │                                  │
      🟢 Local RAG Badge                  Similarity Score
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         │                                                 │
                  Score ≥ 0.75                                      Score < 0.75
           (In-Domain: Constitution & SC)                    (Out-of-Domain: Penal/Statutes)
                         │                                                 │
                   [ LOCAL RAG ]                                 [ ONLINE SEARCH ]
       • Local Ollama / RAG Synthesis                • DuckDuckGo + Wikipedia + Gemini
       • 🟢 Green Lock Badge                         • 🔵 Blue Cloud Badge
       • Constitutional / Case Citations             • Live Web Citations & Mappings
```

---

## 🚀 Quickstart & Local Execution

### Prerequisites
- Python 3.10+ (Tested on Python 3.13)
- Node.js 18+ and npm
- (Optional) [Ollama](https://ollama.ai) with `llama3` or `mistral` pulled for local generative inference.

### 1. Backend Setup & Ingestion
```powershell
# Run the automated PowerShell setup script (creates .venv, installs dependencies)
powershell -ExecutionPolicy Bypass -File .\setup.ps1

# Ingest and embed the complete Indian legal corpus into ChromaDB
.\.venv\Scripts\python.exe backend\ingest.py

# Launch the FastAPI Agentic Router server (port 8000)
.\.venv\Scripts\uvicorn.exe backend.main:app --host 127.0.0.1 --port 8000 --reload
```

### 2. Frontend Setup
In a second terminal:
```bash
# Install frontend dependencies
npm install

# Start the Vite React development server (port 3000)
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 📡 API Reference

### Health Check
`GET /health`
Returns the operational status of the vector store, ChromaDB indexed vector count, and model connectivity.

### Chat Router
`POST /api/chat`
```json
{
  "query": "What did Kesavananda Bharati decide regarding basic structure?",
  "role": "advocate",
  "history": []
}
```

Response:
```json
{
  "text": "### 🏛️ Constitutional & Jurisprudential Summary...",
  "source": "local_rag",
  "confidence_score": 0.829,
  "citations": [
    "[supreme_court_judgments.pdf | Page 0 | Score: 0.83] LANDMARK SC: KESAVANANDA BHARATI v. STATE OF KERALA..."
  ]
}
```

---

## 📚 Academic & Research Foundations

This codebase implements the methodology described in:
> *"A Calibrated Hybrid Router Architecture for Privacy-Preserving and Verifiable Legal Information Retrieval in the Indian Judicial Context"*

Key experimental metrics logged on every query:
- Retrieval Latency (`ms`)
- Cosine Distance & Lexical Corroboration Score
- Routing Decision Boundary Evaluation ($\tau = 0.75$)
- Citation Provenance & Verifiability Ratio

---

## 📜 License
MIT License. Created for academic and educational research.
