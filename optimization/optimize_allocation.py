import pandas as pd
import numpy as np

def simulate_supply(df: pd.DataFrame, seed: int) -> pd.DataFrame:
    """
    Simulate available drivers per zone for a given hour.
    """
    np.random.seed(seed)
    df = df.copy()
    df["available_drivers"] = (
        df["predicted_demand"]
        * np.random.uniform(0.6, 1.4, size=len(df))
    ).astype(int)

    df["gap"] = df["available_drivers"] - df["predicted_demand"]
    return df


def compute_reallocation(zone_df: pd.DataFrame, hour: int) -> list[dict]:
    """
    Greedy reallocation of drivers from surplus to deficit zones.
    """
    records = []

    surplus = zone_df[zone_df["gap"] > 0].copy()
    deficit = zone_df[zone_df["gap"] < 0].copy()
    deficit["need"] = -deficit["gap"]

    for _, s in surplus.iterrows():
        available = s["gap"]

        for idx, d in deficit.iterrows():
            if available <= 0 or d["need"] <= 0:
                continue

            moved = min(available, d["need"])

            records.append({
                "hour": hour,
                "source_zone": s["zone_id"],
                "destination_zone": d["zone_id"],
                "drivers_moved": int(moved)
            })

            available -= moved
            deficit.at[idx, "need"] -= moved

    return records


def optimize_allocation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run hour-wise supply simulation and driver reallocation.
    """
    all_records = []

    for hour in sorted(df["hour"].unique()):
        hour_df = df[df["hour"] == hour]

        zone_demand = (
            hour_df.groupby("zone_id")["predicted_demand"]
            .sum()
            .reset_index()
        )

        zone_supply = simulate_supply(zone_demand, seed=hour)
        records = compute_reallocation(zone_supply, hour)

        all_records.extend(records)

    return pd.DataFrame(all_records)
