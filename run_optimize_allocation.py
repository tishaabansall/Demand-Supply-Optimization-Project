import pandas as pd
from optimize_allocation import optimize_allocation

df = pd.read_csv("data/with_predictions.csv")

result = optimize_allocation(df)
result.to_csv("outputs/optimized_allocation.csv", index=False)

print("Optimized allocation generated")
print(result.head())
