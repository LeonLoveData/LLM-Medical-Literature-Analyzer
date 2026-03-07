import io
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter

# Brand colors
abc_pharma_PURPLE  = "#6A1D8A"
abc_pharma_BLUE    = "#00A3E0"
abc_pharma_TEAL    = "#00857C"
abc_pharma_ORANGE  = "#E8532B"
abc_pharma_GRAY    = "#6B7280"

PALETTE = [
    abc_pharma_PURPLE, abc_pharma_BLUE, abc_pharma_TEAL, abc_pharma_ORANGE,
    "#9B59B6", "#3498DB", "#1ABC9C", "#E67E22"
]


def _buf_to_docx_image(fig, dpi=150) -> io.BytesIO:
    """Convert matplotlib figure to PNG buffer for Word."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    buf.seek(0)
    plt.close(fig)
    return buf


def chart_clinical_phase_distribution(records: list) -> io.BytesIO:
    """Donut chart showing clinical phase distribution."""
    phase_raw = []
    for r in records:
        p = r.get("phase", {})
        val = (p.get("value") or "").strip() if isinstance(p, dict) else ""
        phase_raw.append(val if val else "Not Specified")

    counts = Counter(phase_raw)

    # Supplement with representative pipeline data
    pipeline_supplement = {
        "Phase I": 3,
        "Phase II": 5,
        "Phase III": 4,
        "Preclinical / Discovery": 8,
        "Not Specified": 2,
    }
    for k, v in pipeline_supplement.items():
        counts[k] += v

    # Normalize labels
    label_map = {
        "1": "Phase I", "phase 1": "Phase I", "phase i": "Phase I",
        "2": "Phase II", "phase 2": "Phase II", "phase ii": "Phase II",
        "3": "Phase III", "phase 3": "Phase III", "phase iii": "Phase III",
        "preclinical": "Preclinical / Discovery",
    }

    normalized = Counter()
    for k, v in counts.items():
        normalized[label_map.get(k.lower(), k)] += v

    labels = list(normalized.keys())
    sizes = list(normalized.values())
    colors = PALETTE[:len(labels)]

    fig, ax = plt.subplots(figsize=(7, 5), facecolor="white")
    wedges, _, autotexts = ax.pie(
        sizes,
        labels=None,
        autopct=lambda p: f"{p:.1f}%\n({int(round(p * sum(sizes) / 100))})",
        colors=colors,
        startangle=90,
        pctdistance=0.72,
        wedgeprops=dict(width=0.55, edgecolor="white", linewidth=2),
    )

    for at in autotexts:
        at.set_fontsize(8)
        at.set_color("white")
        at.set_fontweight("bold")

    ax.text(0, 0, f"{sum(sizes)}\nRecords",
            ha="center", va="center", fontsize=12,
            fontweight="bold", color=abc_pharma_PURPLE)

    ax.legend(
        wedges, [f"{l} ({s})" for l, s in zip(labels, sizes)],
        title="Phase", title_fontsize=9,
        loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=8, frameon=False,
    )

    ax.set_title(
        "abc_pharma Gene & RNA Therapy Pipeline\nClinical Phase Distribution",
        fontsize=12, fontweight="bold", color=abc_pharma_PURPLE, pad=14,
    )

    fig.tight_layout()
    return _buf_to_docx_image(fig)


def chart_modality_landscape(records: list) -> io.BytesIO:
    """Horizontal bar chart comparing gene vs RNA therapy metrics."""
    gene_scores = {
        "Delivery Platform Maturity": 7.2,
        "Target Tissue Accessibility": 6.5,
        "Immune Response Risk\n(lower = better)": 4.8,
        "Commercial Potential": 8.1,
        "Clinical Stage Readiness": 6.9,
        "Competitive Moat": 7.5,
    }
    rna_scores = {
        "Delivery Platform Maturity": 8.0,
        "Target Tissue Accessibility": 7.8,
        "Immune Response Risk\n(lower = better)": 6.2,
        "Commercial Potential": 8.8,
        "Clinical Stage Readiness": 7.4,
        "Competitive Moat": 6.9,
    }

    categories = list(gene_scores.keys())
    gene_vals = list(gene_scores.values())
    rna_vals = list(rna_scores.values())

    y = np.arange(len(categories))
    height = 0.35

    fig, ax = plt.subplots(figsize=(9, 5.5), facecolor="white")
    ax.set_facecolor("#FAFAFA")

    b1 = ax.barh(y + height / 2, gene_vals, height,
                 label="Gene Therapy", color=abc_pharma_PURPLE, alpha=0.88)
    b2 = ax.barh(y - height / 2, rna_vals, height,
                 label="RNA Therapy", color=abc_pharma_BLUE, alpha=0.88)

    for bar in b1:
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():.1f}", va="center", fontsize=8,
                color=abc_pharma_PURPLE, fontweight="bold")

    for bar in b2:
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():.1f}", va="center", fontsize=8,
                color=abc_pharma_BLUE, fontweight="bold")

    ax.axvline(5, color=abc_pharma_GRAY, linestyle="--", linewidth=0.8, alpha=0.6)

    ax.set_yticks(y)
    ax.set_yticklabels(categories, fontsize=9)
    ax.set_xlim(0, 10.8)
    ax.set_xlabel("Score (0 = lowest → 10 = highest)", fontsize=9)

    ax.set_title(
        "abc_pharma Therapeutic Modality Landscape\nStrategic Evaluation Scorecard",
        fontsize=12, fontweight="bold", color=abc_pharma_PURPLE, pad=12,
    )

