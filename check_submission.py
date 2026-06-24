import pandas as pd

df = pd.read_csv("output/submission.csv")

print("Rows:", len(df))
print("Unique ranks:", df["rank"].nunique())
print("Unique candidates:", df["candidate_id"].nunique())