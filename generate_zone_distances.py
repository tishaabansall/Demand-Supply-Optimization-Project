import pandas as pd
import numpy as np

zones = ["Central", "North", "South", "East", "West" , "Airport"]

np.random.seed(42)  

n = len(zones)
distances = np.random.randint(2, 15, size=(n, n))

distances = (distances + distances.T) // 2

# to ensure that diagonal must be zero
np.fill_diagonal(distances, 0)

df = pd.DataFrame(distances, index=zones, columns=zones)

df.to_csv("data/zone_distances.csv")

print("zone_distances.csv generated")
