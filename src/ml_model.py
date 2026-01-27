import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

df = pd.read_csv("logs/access_log.csv")

df["frequency"] = df.groupby("endpoint")["endpoint"].transform("count")
df["hit_ratio"] = df.groupby("endpoint")["cache_hit"].transform("mean")

X = df[["frequency", "hit_ratio"]]
y = df["cache_hit"]

model = LogisticRegression()
model.fit(X, y)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/reuse_predictor.pkl")

print("✅ ML model trained and saved")
