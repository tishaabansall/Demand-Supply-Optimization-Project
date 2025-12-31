import pandas as pd

from analysis.gap_analysis import (
    compute_baseline_prediction,
    compute_demand_gap,
    identify_pain_zones,
    identify_worst_hours
)

from optimization.optimize_allocation import optimize_allocation


def run_gap_analysis() -> dict:
    df = pd.read_csv("data/urban_logistics.csv")

    baseline = compute_baseline_prediction(df)
    df = df.merge(baseline, on=["zone_id", "hour"])

    df = compute_demand_gap(df)

    pain_zones = identify_pain_zones(df).reset_index()
    worst_hours = identify_worst_hours(df)

    return {
        "gap_table": df,
        "pain_zones": pain_zones,
        "worst_hours": worst_hours
    }


def run_optimization() -> pd.DataFrame:
    df = pd.read_csv("data/with_predictions.csv")
    result = optimize_allocation(df)
    return result
