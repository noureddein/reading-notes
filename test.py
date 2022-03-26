import csv
import numpy as np

with open('winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))

wines = np.array(wines[1:], dtype=float)

print(wines.dtype)
wines[:, 11] + 10
print(wines[: 11])
