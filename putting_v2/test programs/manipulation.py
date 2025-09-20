import pandas as pd

df = pd.read_csv("grip_measurements1.csv")
df[df > 3] = pd.NA

df.to_csv("no_highs.csv")