import pandas as pd

version = 1

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
                value = int(input("Distance: ")) ; grips[grip].append(value)
                break
            except ValueError:
                continue

# Save to csv
df = pd.DataFrame(grips)
df.to_csv("analyses/grip_measurements{version}.csv", index=False)
