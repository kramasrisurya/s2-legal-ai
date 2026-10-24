# S2 Legal AI Pro — Manuscript Figures & Data Visualizations

This directory contains the complete set of publication-grade figures, architectural flowcharts, empirical plots, and UI artifact placeholders for the research paper:

> **"Router-Based Agentic Retrieval-Augmented Generation for Jurisprudential Reasoning and Multi-Tier Statutory Fallback"**

---

## 1. Inventory of Manuscript Figures

| Figure File | Format | Section in Paper | Academic Description |
| :--- | :---: | :--- | :--- |
| **`fig1_system_architecture.mmd`** | Mermaid / Vector | Methodology (System Architecture) | End-to-end multi-tier architecture showing the React client, FastAPI gateway, ChromaDB dense retrieval, and dynamic routing to Local RAG vs. Gemini Cloud Fallback. |
| **`fig2_ingestion_pipeline.mmd`** | Mermaid / Vector | Methodology (Corpus Ingestion) | Offline document processing pipeline: PDF extraction (`PyPDFLoader`), semantic chunking (`RecursiveCharacterTextSplitter`), `bge-small-en-v1.5` embeddings, and ChromaDB persistent storage. |
| **`fig3_routing_flowchart.mmd`** | Mermaid / Vector | Methodology (Decision Gate) | Agentic routing decision tree highlighting the central $\tau = 0.75$ cosine similarity decision boundary and dual-path fallback mechanisms. |
| **`fig4_latency_comparison.png`** | PNG (300 DPI) | Results & Discussion (Latency) | Grouped bar chart comparing Mean, Median, and 95th-percentile ($p_{95}$) latencies between Local Inference ($1,913\,\text{ms}$) and Cloud Grounding ($1,860\,\text{ms}$) with SEM error bars. |
| **`fig5_routing_confidence.png`** | PNG (300 DPI) | Results & Discussion (Accuracy) | Scatter plot mapping retrieval confidence scores across 50 benchmark queries, illustrating the $\tau = 0.75$ decision boundary, operating zones, and 5 cross-domain edge cases ($90.0\%$ accuracy). |
| **`fig6a_ui_local.png`** | PNG (Placeholder) | System Implementation & UI | User interface screenshot showing the green **"Local RAG (Verified Context)"** badge and expanded source citations accordion. |
| **`fig6b_ui_cloud.png`** | PNG (Placeholder) | System Implementation & UI | User interface screenshot showing the blue **"Cloud Agent (Search Grounded)"** badge for modern statute research queries. |

---

## 2. Instructions for Capturing UI Screenshots (Figure 6)

The React frontend is running locally at **`http://localhost:3000`** with the FastAPI backend active at **`http://127.0.0.1:8000`**. Follow these instructions to capture the final two figures:

### A. Figure 6a: Local RAG (Verified Context) Screenshot
1. Open your browser and navigate to **`http://localhost:3000`**.
2. In the query input box, enter the following in-domain constitutional query:
   ```text
   What are the provisions for the writ of Habeas Corpus under Article 32 of the Constitution?
   ```
3. Submit the query.
4. Verify that the response displays a green badge reading:
   $$\boxed{\text{🔒 Local RAG (Verified Context)}}$$
5. Click on the **"View Source Documents"** accordion below the text to expand the monospaced source citations block (displaying references to `the_constitution_of_india_authoritative_edition.pdf` and `supreme_court_judgments.pdf`).
6. Capture a clean browser screenshot of the chat message and save it as:
   ```text
   paper_figures/fig6a_ui_local.png
   ```

---

### B. Figure 6b: Cloud Agent (Search Grounded) Screenshot
1. In the same chat interface, enter the following out-of-domain modern statute query:
   ```text
   What is the punishment for cheating under the new Bharatiya Nyaya Sanhita?
   ```
2. Submit the query.
3. Verify that the response displays a blue badge reading:
   $$\boxed{\text{🌐 Cloud Agent (Search Grounded)}}$$
4. Confirm that the response provides live grounded statutory analysis (addressing Section 318 BNS / transitional provisions) with an empty local citation accordion.
5. Capture a clean browser screenshot of the message and save it as:
   ```text
   paper_figures/fig6b_ui_cloud.png
   ```

---

## 3. How to Regenerate Figures & Export Vector Graphics

### Regenerating Python Plots (300 DPI)
To re-run the chart generation script against [`backend/evaluation_results.csv`](file:///c:/Projects/s2-legal-ai/backend/evaluation_results.csv):
```powershell
python backend/generate_charts.py
```

### Rendering Mermaid Diagrams to Vector PDF / SVG
If you have the Mermaid CLI (`@mermaid-js/mermaid-cli`) installed:
```powershell
# Export Figure 1 to Vector PDF
npx @mermaid-js/mermaid-cli -i paper_figures/fig1_system_architecture.mmd -o paper_figures/fig1_system_architecture.pdf -b transparent

# Export Figure 2 to Vector PDF
npx @mermaid-js/mermaid-cli -i paper_figures/fig2_ingestion_pipeline.mmd -o paper_figures/fig2_ingestion_pipeline.pdf -b transparent

# Export Figure 3 to Vector PDF
npx @mermaid-js/mermaid-cli -i paper_figures/fig3_routing_flowchart.mmd -o paper_figures/fig3_routing_flowchart.pdf -b transparent
```

Alternatively, copy-paste the contents of `.mmd` files directly into [Mermaid Live Editor](https://mermaid.live) to download crisp SVG or PNG figures.

---

## 4. LaTeX Inclusion Snippets for Academic Manuscript

```latex
% Figure 4: Latency Comparison
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.92\linewidth]{paper_figures/fig4_latency_comparison.png}
  \caption{End-to-end response latency comparison (mean, median, and $p_{95}$) across 50 benchmark queries. Error bars represent the Standard Error of the Mean (SEM).}
  \label{fig:latency_comparison}
\end{figure}

% Figure 5: Decision Gate & Routing Confidence
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\linewidth]{paper_figures/fig5_routing_confidence.png}
  \caption{Distribution of retrieval confidence scores across the 50-query standardized evaluation dataset. The decision boundary ($\tau = 0.75$) cleanly bifurcates in-domain constitutional queries from out-of-domain modern statutes, achieving $90.0\%$ classification accuracy with five realistic cross-statute boundary cases.}
  \label{fig:routing_confidence}
\end{figure}
```
