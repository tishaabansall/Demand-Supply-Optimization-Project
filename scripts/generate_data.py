import pandas as pd
import numpy as np
import os

np.random.seed(42)

zones = ["Central", "North", "South", "East", "West", "Airport"]
hours = range(24)
days = range(7)

rows = []

for zone in zones:
    for day in days:
        for hour in hours:

            # Base demand by zone
            base_demand = {
                "Central": 60,
                "Airport": 50,
                "North": 30,
                "South": 25,
                "East": 20,
                "West": 20
            }[zone]

            # Hour-based adjustment
            if 8 <= hour <= 10 or 17 <= hour <= 20:
                demand = base_demand + np.random.randint(20, 40)
            else:
                demand = base_demand + np.random.randint(-10, 15)

            supply = int(demand * np.random.uniform(0.6, 0.9))

            wait_time = max(2, (demand - supply) * 0.4)

            rows.append([
                zone,
                hour,
                day,
                max(demand, 5),
                max(supply, 3),
                round(wait_time, 2)
            ])

df = pd.DataFrame(
    rows,
    columns=[
        "zone_id",
        "hour",
        "day",
        "historical_demand",
        "available_supply",
        "avg_wait_time"
    ]
)

os.makedirs("data", exist_ok=True)
df.to_csv("data/urban_logistics.csv", index=False)

print("Dataset generated:", df.shape)
