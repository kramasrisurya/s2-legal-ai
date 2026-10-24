# S2 Legal AI Pro — Manuscript Figures & Data Visualizations (Simplified)

This directory contains clean, streamlined, publication-ready figures for the research paper:

> **"Router-Based Agentic Retrieval-Augmented Generation for Jurisprudential Reasoning and Multi-Tier Statutory Fallback"**

---

## 1. Inventory of Figures

| Figure File | Format | Section | Summary |
| :--- | :---: | :--- | :--- |
| **`fig1_system_architecture.mmd`** | Mermaid | System Architecture | Simple end-to-end data flow: User $\rightarrow$ React UI $\rightarrow$ FastAPI Router $\rightarrow$ ChromaDB $\rightarrow$ Decision Gate ($\tau \ge 0.75$) $\rightarrow$ Local RAG vs. Gemini Fallback. |
| **`fig2_ingestion_pipeline.mmd`** | Mermaid | Corpus Ingestion | 5-step pipeline: Legal PDFs $\rightarrow$ PyPDFLoader $\rightarrow$ Text Splitter $\rightarrow$ `bge-small-en-v1.5` $\rightarrow$ ChromaDB. |
| **`fig3_routing_flowchart.mmd`** | Mermaid | Decision Gate | Decision tree with central similarity diamond ($\ge 0.75$) routing to Local Model (Ollama) or Cloud Fallback (Gemini + Search). |
| **`fig4_latency_comparison.png`** | PNG (300 DPI) | Results (Latency) | Clean grouped bar chart comparing Mean & Median latency between Local RAG ($1,913\,\text{ms}$) and Cloud Fallback ($1,860\,\text{ms}$). |
| **`fig5_routing_confidence.png`** | PNG (300 DPI) | Results (Accuracy) | Minimalist scatter plot mapping confidence scores across 50 benchmark queries with the $\tau = 0.75$ decision threshold and 5 edge cases ($90.0\%$ accuracy). |
| **`fig6a_ui_local.png`** | PNG (Placeholder) | System UI | Screenshot of green **"Local RAG (Verified Context)"** badge with citation accordion open. |
| **`fig6b_ui_cloud.png`** | PNG (Placeholder) | System UI | Screenshot of blue **"Cloud Agent (Search Grounded)"** badge. |

---

## 2. Capturing the UI Screenshots (Figure 6)

Navigate to **`http://localhost:3000`** in your browser:

### Figure 6a: Local RAG Screenshot
1. Ask:
   ```text
   What are the provisions for the writ of Habeas Corpus under Article 32 of the Constitution?
   ```
2. Verify the green **"Local RAG (Verified Context)"** badge appears.
3. Click **"View Source Documents"** to open the citation accordion.
4. Take a screenshot and save as:
   ```text
   paper_figures/fig6a_ui_local.png
   ```

### Figure 6b: Cloud Fallback Screenshot
1. Ask:
   ```text
   What is the punishment for cheating under the new Bharatiya Nyaya Sanhita?
   ```
2. Verify the blue **"Cloud Agent (Search Grounded)"** badge appears.
3. Take a screenshot and save as:
   ```text
   paper_figures/fig6b_ui_cloud.png
   ```

---

## 3. How to Regenerate Figures
```powershell
python backend/generate_charts.py
```
