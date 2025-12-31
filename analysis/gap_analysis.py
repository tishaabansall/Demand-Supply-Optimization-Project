import pandas as pd

def compute_baseline_prediction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute average historical demand per zone and hour.
    """
    baseline = (
        df.groupby(["zone_id", "hour"])["historical_demand"]
        .mean()
        .reset_index()
        .rename(columns={"historical_demand": "predicted_demand"})
    )
    return baseline


def compute_demand_gap(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add demand_gap column = predicted_demand - available_supply
    """
    df = df.copy()
    df["demand_gap"] = df["predicted_demand"] - df["available_supply"]
    return df


def identify_pain_zones(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rank zones by total and average shortage.
    """
    pain_zones = (
        df[df["demand_gap"] > 0]
        .groupby("zone_id")
        .agg(
            total_shortage=("demand_gap", "sum"),
            avg_shortage=("demand_gap", "mean"),
            shortage_hours=("demand_gap", "count")
        )
        .sort_values(by="total_shortage", ascending=False)
    )
    return pain_zones


def identify_worst_hours(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rank hours by total demand gap.
    """
    hourly_pain = (
        df[df["demand_gap"] > 0]
        .groupby("hour")["demand_gap"]
        .sum()
        .reset_index()
        .sort_values(by="demand_gap", ascending=False)
    )
    return hourly_pain
