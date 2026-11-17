import sqlite3
import pandas as pd

con = sqlite3.connect("practice.db")
turbines = pd.read_sql("SELECT * FROM turbines", con)
readings = pd.read_sql("SELECT * FROM readings", con)
readings["read_date"] = pd.to_datetime(readings["read_date"])

turbines_k = turbines.rename(columns={"id": "turbine_id"})
df = readings.merge(turbines_k, on="turbine_id", how="left")

print(df)
print()
print(df.head())
print()
print(df.describe())
print()
print(df.info())
print()
print(df.dtypes)
print()
print(df.isna().sum())