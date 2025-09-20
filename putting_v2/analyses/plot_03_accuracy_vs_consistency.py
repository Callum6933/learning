import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
import sys

if len(sys.argv) != 2:
        sys.exit("Usage: python plot_03_accuracy_vs_consistency.py input.csv")

def main():
    df = pd.read_csv(sys.argv[1], index_col=0)
    df["range"] = df["max"] - df["min"]  # consistency proxy; lower is better

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.scatter(
        df["mean"], df["range"], s=90, color="#4C78A8", edgecolor="black", alpha=0.9
    )
    for grip, row in df.iterrows():
        ax.text(row["mean"] + 0.02, row["range"] + 0.02, grip, fontsize=9)

    ax.axvline(df["mean"].median(), color="0.7", linestyle="--", linewidth=1)
    ax.axhline(df["range"].median(), color="0.7", linestyle="--", linewidth=1)

    xpad = 0.3
    ypad = 0.3
    ax.set_xlim(max(0, df["mean"].min() - xpad), df["mean"].max() + xpad)
    ax.set_ylim(max(0, df["range"].min() - ypad), df["range"].max() + ypad)

    ax.set_xlabel("Accuracy (mean distance, lower is better)")
    ax.set_ylabel("Consistency (range = max - min, lower is better)")
    ax.set_title(
        "Accuracy vs consistency by putting grip\n(lower-left quadrant is best)"
    )
    fig.tight_layout()

    i = 0

    while True:
        filename = f"03_accuracy_vs_consistency_v{i}.png"
        if os.path.exists(filename):
            i += 1
        else:
            break
   
    outfile = Path(filename)
    fig.savefig(outfile, dpi=200)


if __name__ == "__main__":
    main()
