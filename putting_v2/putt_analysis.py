import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python putt_analysis.py filename.csv")

try:
    df = pd.read_csv(sys.argv[1])
except Exception as e:
    sys.exit(f"Exception: {e}")

std_dev = df.std().round(2)

# Load csv into dataframe
stats_df = pd.DataFrame({
    "mean": df.mean().round(2),
    "median": df.median().round(2),
    "min": df.min().round(2),
    "max": df.max().round(2),
    "std dev": std_dev,
    "std err": round(std_dev/np.sqrt(8), 10),
})

# Export data
i = 0

while True:
    filename = f"analyses/metrics{i}.csv"

    if os.path.exists(filename):
        i += 1
    else:
        break

stats_df.to_csv(filename)