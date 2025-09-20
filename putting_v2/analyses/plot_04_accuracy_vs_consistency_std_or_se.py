import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python plot_04_accuracy_vs_consistency_std_or_se.py input.csv")

def main():
    try:
        df = pd.read_csv(sys.argv[1], index_col=0)
    except Exception as e:
        sys.exit(f"Exception: {e}")

    # Ensure numeric
    for col in ["mean", "median", "min", "max", "std", "se", "n"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Pick consistency metric: prefer SE if present, else STD, else estimate STD from range/6
    note = None
    metric_used = None
    if "se" in df.columns and df["se"].notna().all():
        consistency = df["se"].copy()
        metric_used = "Standard error"
    elif "std" in df.columns and df["std"].notna().all():
        consistency = df["std"].copy()
        metric_used = "Standard deviation"
    elif (
        "std" in df.columns
        and "n" in df.columns
        and df[["std", "n"]].notna().all().all()
        and (df["n"] > 0).all()
    ):
        consistency = df["std"] / np.sqrt(df["n"])
        metric_used = "Standard error (computed from std and n)"
        note = "Computed SE = std / sqrt(n)."
    elif {"min", "max"}.issubset(df.columns):
        consistency = (df["max"] - df["min"]) / 6.0
        metric_used = "Estimated std dev from range"
        note = "Estimated std ≈ (max - min) / 6 (assumes roughly normal spread)."
    else:
        sys.exit(
            "metrics.csv must include either 'se' or 'std' (and optionally 'n'), or both 'min' and 'max' to estimate std."
        )

    # Prepare plot
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(7, 5))

    x = df["mean"]
    y = consistency

    ax.scatter(x, y, s=100, color="#4C78A8", edgecolor="black", alpha=0.9)

    # Label points
    for grip, row in df.iterrows():
        ax.text(row["mean"] + 0.02, y.loc[grip] + 0.02, grip, fontsize=9)

    # Quadrant medians
    ax.axvline(x.median(), color="0.7", linestyle="--", linewidth=1)
    ax.axhline(y.median(), color="0.7", linestyle="--", linewidth=1)

    # Axis limits with padding
    xpad = 0.3
    ypad = 0.15
    ax.set_xlim(max(0, float(x.min() - xpad)), float(x.max() + xpad))
    ax.set_ylim(max(0, float(y.min() - ypad)), float(y.max() + ypad))

    ax.set_xlabel("Accuracy (mean distance from hole, ft; lower is better)")
    ax.set_ylabel(f"Consistency ({metric_used}, ft; lower is better)")
    ax.set_title(
        "Accuracy vs consistency by putting grip\n(based on std dev / std error)"
    )

    if note:
        ax.text(
            0.99,
            0.01,
            note,
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=8,
            color="0.4",
        )

    fig.tight_layout()

    i = 0

    while True:
        filename = f"04_accuracy_vs_consistency_std_se_v{i}.png"
        if os.path.exists(filename):
            i += 1
        else:
            break
   
    outfile = Path(f"output/{filename}")
    fig.savefig(outfile, dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
