import pandas as pd

# load data
df = pd.read_csv("data/urban_logistics.csv")

baseline = (
    df
    .groupby(["zone_id", "hour"])["historical_demand"]
    .mean()
    .reset_index()
    .rename(columns={"historical_demand": "baseline_demand"})
)

# merge back
df_baseline = df.merge(baseline, on=["zone_id", "hour"])

print(df_baseline.head())
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(
    df_baseline["historical_demand"],
    df_baseline["baseline_demand"]
)

print("Baseline MAE:", round(mae, 2))
