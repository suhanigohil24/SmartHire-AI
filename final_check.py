import pandas as pd

df = pd.read_csv("output/submission.csv")

print("Rows:", len(df))
print("Unique ranks:", df["rank"].nunique())
print("Unique candidates:", df["candidate_id"].nunique())
print("Columns:", list(df.columns))

print("Duplicate IDs:",
      df["candidate_id"].duplicated().sum())

print("Duplicate ranks:",
      df["rank"].duplicated().sum())

print(
    "Scores descending:",
    df["score"].is_monotonic_decreasing
)