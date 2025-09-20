import pandas as pd
import os

"""
How to use:
- Run 'python3 putt_measurements.py'
- Run 'python3 putt_analysis.py data/measurements.csv'
- Run 'python3 plot_01_mean_with_range.py data/metrics.csv'
"""

# Create dict for variables
grips = {
    "claw": [],
    "normal": [],
    "japanese": [],
}
# Get manual input for each grip, one at a time
for grip in grips:
    print(f"Collecting data for {grip}:")

    for i in range(10):
        while True:
            try:
                value = int(input("Distance: "))
                grips[grip].append(value)
                break
            except ValueError:
                continue

# Save to csv
df = pd.DataFrame(grips)

i = 0

while True:
    filename = f"measurements{i}.csv"
    if os.path.exists(filename):
        i += 1
    else:
        break

df.to_csv(f"data/{filename}.csv", index=False)
print(f"File saved as: data/{filename}")
