import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/urban_logistics.csv")

# encode zone
le = LabelEncoder()
df["zone_encoded"] = le.fit_transform(df["zone_id"])


df["lag_demand"] = df.groupby("zone_id")["historical_demand"].shift(1)
df = df.dropna()

X = df[["zone_encoded", "hour", "day", "lag_demand"]]
y = df["historical_demand"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)

print("ML Model MAE:", round(mae, 2))
df["predicted_demand"] = model.predict(
    df[["zone_encoded", "hour", "day", "lag_demand"]]
)

df.to_csv("data/with_predictions.csv", index=False)
print("Saved predictions.")
