import pandas as pd

try:
    df = pd.read_csv("energy_cleaned.csv", encoding="utf-16")
except Exception:
    df = pd.read_csv("energy_cleaned.csv", encoding="utf-8")

print("--- DATAFRAME HEAD ---")
print(df.head())

print("\n--- NUMERIC SUMMARY (STATISTICS) ---")
print(df.describe())

print("\n--- REGION DISTRIBUTION ---")
print(df['Region'].value_counts())

print("\n--- RENEWABLE ENERGY THRESHOLD ANALYSIS ---")

high_renew = df[df["%Renewable"] > 50]
print("Countries with >50% renewable energy:", len(high_renew))

high_renew_60 = df[df["%Renewable"] > 60]
high_renew_70 = df[df["%Renewable"] > 70]

print("Countries with >60% renewable energy:", len(high_renew_60))
print("Countries with >70% renewable energy:", len(high_renew_70))

print("\n--- REGIONAL ADOPTION METRICS ---")

region_avg = df.groupby("Region")["%Renewable"].mean()
print(region_avg)