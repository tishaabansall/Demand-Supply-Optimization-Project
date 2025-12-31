import pandas as pd
import numpy as np

np.random.seed(0)

zones = ["Central", "North", "South", "East", "West", "Airport"]

data = {
    "zone": zones,
    "orders": np.random.randint(50, 200, size=len(zones)),
    "available_staff": np.random.randint(20, 100, size=len(zones))
}

df = pd.DataFrame(data)
df.to_csv("data/zone_request.csv", index=False)

print("zone_request.csv created")
