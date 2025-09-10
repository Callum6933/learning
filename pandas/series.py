import pandas as pd

patients = {"John": "Liver Disease", "Alice": "Diabetes", "Bob": "Healthy"}

myvar = pd.Series(patients)

print(myvar["Alice"])