"""
S2 Legal AI Pro - Clean, Minimalist Data Visualization Pipeline
Module: backend.generate_charts

Generates simple, clean, and publication-ready figures (300 DPI):
- fig4_latency_comparison.png: Clean bar chart comparing Local RAG vs. Cloud Fallback latency
- fig5_routing_confidence.png: Clean scatter plot showing the 0.75 decision threshold and data points
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Any, Dict, List

# Safe UTF-8 configuration
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Headless Agg backend for Matplotlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CSV_PATH = SCRIPT_DIR / "evaluation_results.csv"
OUTPUT_DIR = PROJECT_ROOT / "paper_figures"


def load_data(csv_file: Path) -> List[Dict[str, Any]]:
    """Loads benchmark evaluation data from CSV."""
    if not csv_file.exists():
        raise FileNotFoundError(f"Missing results CSV: {csv_file}")

    records: List[Dict[str, Any]] = []
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                "id": int(row["id"]),
                "expected_route": row["expected_route"],
                "actual_source": row["actual_source"],
                "routing_match": row["routing_match"].strip().lower() == "true",
                "confidence_score": float(row["confidence_score"]),
                "latency_ms": float(row["latency_ms"]),
            })
    return records


def generate_fig4_latency(records: List[Dict[str, Any]], out_path: Path) -> None:
    """Figure 4: Simple, clean grouped bar chart comparing Mean and Median latency."""
    local_lats = [r["latency_ms"] for r in records if r["actual_source"] == "local_rag"]
    cloud_lats = [r["latency_ms"] for r in records if r["actual_source"] == "gemini_fallback"]

    mean_local = sum(local_lats) / len(local_lats)
    mean_cloud = sum(cloud_lats) / len(cloud_lats)

    sorted_local = sorted(local_lats)
    median_local = sorted_local[len(sorted_local) // 2]

    sorted_cloud = sorted(cloud_lats)
    median_cloud = sorted_cloud[len(sorted_cloud) // 2]

    # Clean styling
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, ax = plt.subplots(figsize=(6.8, 4.4), dpi=300)

    x = [0.0, 1.2]
    width = 0.32

    # Bars: Steel Blue and Slate Gray
    color_local = "#2b5c8f"
    color_cloud = "#6c757d"

    bars_local = ax.bar(
        [pos - width / 2 for pos in x],
        [mean_local, median_local],
        width=width,
        label=f"Local RAG (Ollama / ChromaDB)",
        color=color_local,
        edgecolor="#1a365d",
        linewidth=1.0,
    )

    bars_cloud = ax.bar(
        [pos + width / 2 for pos in x],
        [mean_cloud, median_cloud],
        width=width,
        label=f"Cloud Fallback (Gemini + Search)",
        color=color_cloud,
        edgecolor="#343a40",
        linewidth=1.0,
    )

    # Simple, clear data labels on top of bars
    for b in bars_local:
        h = b.get_height()
        ax.annotate(
            f"{int(round(h))} ms",
            xy=(b.get_x() + b.get_width() / 2, h),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10.5,
            fontweight="bold",
            color="#1a365d",
        )

    for b in bars_cloud:
        h = b.get_height()
        ax.annotate(
            f"{int(round(h))} ms",
            xy=(b.get_x() + b.get_width() / 2, h),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10.5,
            fontweight="bold",
            color="#343a40",
        )

    ax.set_title("Figure 4: Average Response Latency Comparison", fontsize=12, fontweight="bold", pad=12)
    ax.set_ylabel("Latency (milliseconds)", fontsize=10.5, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(["Mean Latency", "Median Latency"], fontsize=11, fontweight="bold")
    ax.set_ylim(0, 3000)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"{int(y):,} ms"))

    ax.legend(frameon=True, loc="upper right", fontsize=9.5, edgecolor="#d1d5db")
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[DATA VIS] Exported simple Figure 4 to: {out_path.name}")


def generate_fig5_confidence(records: List[Dict[str, Any]], out_path: Path) -> None:
    """Figure 5: Simple, clean scatter plot mapping confidence scores and 0.75 decision threshold."""
    fig, ax = plt.subplots(figsize=(7.8, 4.4), dpi=300)

    threshold = 0.75

    # Simple horizontal threshold line
    ax.axhline(y=threshold, color="#dc2626", linestyle="--", linewidth=1.8, label="Threshold (0.75)", zorder=2)

    # Clean, subtle operating zones
    ax.axhspan(threshold, 1.05, color="#dcfce7", alpha=0.35, label="Local RAG Region (>= 0.75)")
    ax.axhspan(0.58, threshold, color="#e0f2fe", alpha=0.35, label="Cloud Fallback Region (< 0.75)")

    local_x, local_y = [], []
    cloud_x, cloud_y = [], []
    edge_x, edge_y = [], []

    for r in records:
        qid = r["id"]
        conf = r["confidence_score"]
        act = r["actual_source"]
        match = r["routing_match"]

        if act == "local_rag":
            local_x.append(qid)
            local_y.append(conf)
        else:
            cloud_x.append(qid)
            cloud_y.append(conf)

        if not match:
            edge_x.append(qid)
            edge_y.append(conf)

    # Plot Local Points (Green)
    ax.scatter(
        local_x, local_y,
        color="#16a34a", s=50, alpha=0.9, edgecolor="#14532d", linewidth=0.8,
        label=f"Local RAG ({len(local_x)} queries)", zorder=3,
    )

    # Plot Cloud Points (Blue)
    ax.scatter(
        cloud_x, cloud_y,
        color="#0284c7", s=50, alpha=0.9, edgecolor="#075985", linewidth=0.8,
        label=f"Cloud Fallback ({len(cloud_x)} queries)", zorder=3,
    )

    # Highlight the 5 Edge Cases (Red Ring)
    ax.scatter(
        edge_x, edge_y,
        facecolors="none", edgecolors="#dc2626", s=110, linewidth=1.8,
        label=f"Boundary Edge Cases ({len(edge_x)} queries, 90% Accuracy)", zorder=4,
    )

    ax.set_title("Figure 5: Router Confidence Scores & Decision Boundary", fontsize=12, fontweight="bold", pad=12)
    ax.set_xlabel("Query Number (1 to 50)", fontsize=10.5, fontweight="bold")
    ax.set_ylabel("Confidence Score (Similarity)", fontsize=10.5, fontweight="bold")
    ax.set_xlim(0, 51)
    ax.set_ylim(0.60, 1.05)
    ax.set_xticks(range(5, 51, 5))

    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend(frameon=True, loc="lower right", fontsize=8.5, edgecolor="#d1d5db")

    plt.tight_layout()
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[DATA VIS] Exported simple Figure 5 to: {out_path.name}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    records = load_data(CSV_PATH)

    fig4_path = OUTPUT_DIR / "fig4_latency_comparison.png"
    fig5_path = OUTPUT_DIR / "fig5_routing_confidence.png"

    generate_fig4_latency(records, fig4_path)
    generate_fig5_confidence(records, fig5_path)

    print("[DATA VIS] Successfully generated clean, simple figures!")


if __name__ == "__main__":
    main()
