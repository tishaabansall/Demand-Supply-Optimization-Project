import pandas as pd
import matplotlib.pyplot as plt

# Load optimized dispatch data
df = pd.read_csv("outputs/optimized_allocation.csv")

# to show available hours
print("Available hours:", sorted(df["hour"].unique()))

# to choose hour
hour = int(input("Enter hour to visualize: "))

hour_df = df[df["hour"] == hour]

if hour_df.empty:
    print("No reallocations for this hour.")
else:
    hour_df["label"] = (
        hour_df["source_zone"] + " → " + hour_df["destination_zone"]
    )

    plt.figure(figsize=(12, 5))
    plt.bar(hour_df["label"], hour_df["drivers_moved"])
    plt.title(f"Driver Reallocation at Hour {hour}")
    plt.ylabel("Drivers Moved")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
