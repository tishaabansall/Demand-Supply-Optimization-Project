import pandas as pd

# load data
df = pd.read_csv("data/urban_logistics.csv")


baseline = (
    df.groupby(["zone_id", "hour"])["historical_demand"]
    .mean()
    .reset_index()
    .rename(columns={"historical_demand": "predicted_demand"})
)
df = df.merge(baseline, on=["zone_id", "hour"])

df["gap"] = df["predicted_demand"] - df["available_supply"]

# load distances
distances = pd.read_csv("data/zone_distances.csv", index_col=0)

# choose a single hour to simulate (keep it simple)
HOUR = 18
hour_df = df[df["hour"] == HOUR].copy()

shortage_zones = hour_df[hour_df["gap"] > 0]
surplus_zones = hour_df[hour_df["gap"] < 0]

actions = []

for _, shortage in shortage_zones.iterrows():
    need = shortage["gap"]
    target_zone = shortage["zone_id"]

    # sort surplus zones by distance
    surplus_sorted = surplus_zones.copy()
    surplus_sorted["distance"] = surplus_sorted["zone_id"].apply(
        lambda z: distances.loc[z, target_zone]
    )
    surplus_sorted = surplus_sorted.sort_values("distance")

    for idx, surplus in surplus_sorted.iterrows():
        if need <= 0:
            break

        available = abs(surplus["gap"])
        transfer = min(available, need)

        actions.append({
            "from": surplus["zone_id"],
            "to": target_zone,
            "units_moved": transfer,
            "distance": distances.loc[surplus["zone_id"], target_zone]
        })

        # update gaps
        surplus_zones.loc[idx, "gap"] += transfer
        need -= transfer

print("\nReallocation Actions:")
for a in actions:
    print(a)

initial_shortage = shortage_zones["gap"].sum()
final_shortage = max(0, initial_shortage - sum(a["units_moved"] for a in actions))

print("\nInitial total shortage:", initial_shortage)
print("Final total shortage:", final_shortage)
