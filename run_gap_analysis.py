import pandas as pd

from analysis.gap_analysis import (
    compute_baseline_prediction,
    compute_demand_gap,
    identify_pain_zones,
    identify_worst_hours
)

df = pd.read_csv("data/urban_logistics.csv")

baseline = compute_baseline_prediction(df)
df = df.merge(baseline, on=["zone_id", "hour"])

df = compute_demand_gap(df)

pain_zones = identify_pain_zones(df)
hourly_pain = identify_worst_hours(df)

print(pain_zones.head())
print(hourly_pain.head())
