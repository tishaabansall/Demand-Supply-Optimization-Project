import pandas as pd

demand = pd.read_csv("data/ride_demand.csv")
optimized = pd.read_csv("outputs/optimized_dispatch.csv")

before = demand[["zone", "available_drivers"]].copy()
before["type"] = "Before Optimization"

after = optimized[["to_zone", "drivers_assigned"]].copy()
after.columns = ["zone", "drivers"]
after["type"] = "After Optimization"

comparison = pd.concat([before, after], ignore_index=True)
comparison.to_csv("outputs/allocation_comparison.csv", index=False)

print("allocation_comparison.csv created")
