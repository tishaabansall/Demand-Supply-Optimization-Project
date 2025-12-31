import pandas as pd

zones = ["Central", "North", "South", "East", "West", "Airport"]

# symmetric distance matrix (in km, synthetic)
distance_data = {
    "Central": {"Central": 0, "North": 5, "South": 6, "East": 4, "West": 4, "Airport": 8},
    "North":   {"Central": 5, "North": 0, "South": 7, "East": 6, "West": 5, "Airport": 10},
    "South":   {"Central": 6, "North": 7, "South": 0, "East": 5, "West": 6, "Airport": 9},
    "East":    {"Central": 4, "North": 6, "South": 5, "East": 0, "West": 7, "Airport": 8},
    "West":    {"Central": 4, "North": 5, "South": 6, "East": 7, "West": 0, "Airport": 9},
    "Airport": {"Central": 8, "North": 10,"South": 9, "East": 8, "West": 9, "Airport": 0},
}

distance_df = pd.DataFrame(distance_data)
distance_df.to_csv("data/zone_distances.csv")

print("Zone distance matrix saved.")
