import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python plot_01_mean_with_range.py data/input.csv")

def main():
    df = pd.read_csv(sys.argv[1], index_col=0)
    df = df[["mean", "median", "min", "max"]]

    sns.set_theme(style="whitegrid")
    grips = df.index.tolist()
    means = df["mean"].values
    lower = (df["mean"] - df["min"]).values
    upper = (df["max"] - df["mean"]).values
    x = range(len(grips))

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(
        x,
        means,
        yerr=[lower, upper],
        capsize=8,
        color="#4C78A8",
        alpha=0.85,
        label="Mean",
    )
    ax.scatter(
        x, df["median"].values, marker="D", color="#F58518", zorder=3, label="Median"
    )

    ax.set_xticks(list(x))
    ax.set_xticklabels(grips)
    ax.set_ylabel("Distance from hole (ft)")
    ax.set_title("Putting grips: mean distance with min–max range and median overlay")

    for i, (bar, mean, median) in enumerate(zip(bars, means, df["median"].values)):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            mean + 0.08,
            f"{mean:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )
        ax.text(
            i,
            median - 0.12,
            f"{median:.2f}",
            ha="center",
            va="top",
            fontsize=8,
            color="#F58518",
        )

    ax.legend()
    fig.tight_layout()

    i = 0

    while True:
        filename = f"01_mean_with_range_v{i}.png"
        if os.path.exists(filename):
            i += 1
        else:
            break
    
    outfile = Path(f"output/{filename}")
    fig.savefig(outfile, dpi=200)


if __name__ == "__main__":
    main()
