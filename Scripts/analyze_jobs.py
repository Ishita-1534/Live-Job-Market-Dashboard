import pandas as pd

# Read the jobs data
df = pd.read_csv("../data/jobs.csv")

print("\nTotal Jobs:", len(df))

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Jobs:")
print(df[["Title", "Company", "Location"]].head())

print("\nTop Hiring Companies:")
print(df["Company"].value_counts().head(10))

print("\nTop Hiring Locations:")
print(df["Location"].value_counts().head(10))