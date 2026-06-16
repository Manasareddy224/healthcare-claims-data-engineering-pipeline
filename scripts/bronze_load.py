import pandas as pd
import os

print("Bronze load started")

os.makedirs("data/bronze/members", exist_ok=True)
os.makedirs("data/bronze/providers", exist_ok=True)
os.makedirs("data/bronze/claims", exist_ok=True)

members_df = pd.read_csv("data/raw/members.csv")
providers_df = pd.read_csv("data/raw/providers.csv")
claims_df = pd.read_csv("data/raw/claims.csv")

print("Members Data:")
print(members_df)

print("Providers Data:")
print(providers_df)

print("Claims Data:")
print(claims_df)

members_df.to_csv("data/bronze/members/members_bronze.csv", index=False)
providers_df.to_csv("data/bronze/providers/providers_bronze.csv", index=False)
claims_df.to_csv("data/bronze/claims/claims_bronze.csv", index=False)

print("Bronze load completed successfully")