import pandas as pd

df = pd.read_csv("logs/access_log.csv",
                 names=["key", "hit", "timestamp"])

features = df.groupby("key").agg(
    frequency=("key", "count"),
    hit_ratio=("hit", "mean")
).reset_index()

features.to_csv("data/features.csv", index=False)
