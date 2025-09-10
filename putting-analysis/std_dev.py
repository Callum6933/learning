import numpy as np

japanese = [1, 3, 0.5, 1, 2, 2.5, 0.5, 1, 1]
claw = [3, 2.5, 2, 1, 3, 0.5, 2, 1, 1]

japsd = np.std(japanese, ddof=1)
clawsd = np.std(claw, ddof=1)

n = len(japanese)
japse = japsd / np.sqrt(n)
clawse = clawsd / np.sqrt(n)

japmean = np.mean(japanese)
clawmean = np.mean(claw)

print(f"Japanese Standard Deviation: {round(japsd, 2)}")
print(f"Japanese Standard Error: {round(japse, 2)}")
print(f"Japanese Mean: {round(japmean, 2)}")

print(f"Claw Standard Deviation: {round(clawsd, 2)}")
print(f"Claw Standard Error: {round(clawse, 2)}")
print(f"Claw Mean: {round(clawmean, 2)}")