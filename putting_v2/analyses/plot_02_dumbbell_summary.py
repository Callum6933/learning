import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mlines
from pathlib import Path
import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python plot_02_dumbell_summary.py input.csv")


def main():
    df = pd.read_csv(sys.argv[1], index_col=0)
    df = df[["min", "median", "mean", "max"]]
    df = df.sort_values("mean")  # best (lowest mean) at top

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 5))

    colors = {
        "min": "#54A24B",  # green
        "median": "#F58518",  # orange
        "mean": "#4C78A8",  # blue
        "max": "#E45756",  # red
    }

    y_positions = range(len(df))
    for i, (grip, row) in enumerate(df.iterrows()):
        ax.hlines(
            y=i, xmin=row["min"], xmax=row["max"], color="0.7", linewidth=3, zorder=1
        )
        ax.scatter(
            row["min"], i, s=70, color=colors["min"], edgecolor="black", zorder=2
        )
        ax.scatter(
            row["median"],
            i,
            s=70,
            marker="D",
            color=colors["median"],
            edgecolor="black",
            zorder=3,
        )
        ax.scatter(
            row["mean"],
            i,
            s=70,
            marker="s",
            color=colors["mean"],
            edgecolor="black",
            zorder=3,
        )
        ax.scatter(
            row["max"], i, s=70, color=colors["max"], edgecolor="black", zorder=2
        )
        ax.text(row["max"] + 0.05, i, grip, va="center", fontsize=10)

    ax.set_yticks(list(y_positions))
    ax.set_yticklabels([""] * len(df))  # labels shown as text on the right
    ax.set_xlabel("Distance from hole (ft)")
    ax.set_title("Putting grips: min–median–mean–max summary (lower is better)")
    ax.invert_yaxis()  # best at top due to sorting

    legend_handles = [
        mlines.Line2D(
            [],
            [],
            color=colors["min"],
            marker="o",
            linestyle="None",
            markersize=8,
            label="Min",
        ),
        mlines.Line2D(
            [],
            [],
            color=colors["median"],
            marker="D",
            linestyle="None",
            markersize=8,
            label="Median",
        ),
        mlines.Line2D(
            [],
            [],
            color=colors["mean"],
            marker="s",
            linestyle="None",
            markersize=8,
            label="Mean",
        ),
        mlines.Line2D(
            [],
            [],
            color=colors["max"],
            marker="o",
            linestyle="None",
            markersize=8,
            label="Max",
        ),
        mlines.Line2D([], [], color="0.7", linewidth=3, label="Range (min–max)"),
    ]
    ax.legend(handles=legend_handles, loc="lower right")
    fig.tight_layout()

    i = 0

    while True:
        filename = f"02_dumbbell_summary_v{i}.png"
        if os.path.exists(filename):
            i += 1
        else:
            break
    
    outfile = Path(f"output/{filename}")
    fig.savefig(outfile, dpi=200)


if __name__ == "__main__":
    main()
