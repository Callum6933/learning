import pandas as pd

genomes = {
    "Person": ["Callum", "Luke", "Hairi"],
    "seq": ["ATTG", "TTAC", "CGAA"],
    "rev": []
}

genomes["rev"] = [s[::-1] for s in genomes["seq"]]

df = pd.DataFrame(genomes)

print(df)