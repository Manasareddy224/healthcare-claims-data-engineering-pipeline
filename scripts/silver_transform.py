import pandas as pd
import os

print("Silver transformation started")

os.makedirs("data/silver/claims_cleaned", exist_ok=True)

members_df = pd.read_csv("data/bronze/members/members_bronze.csv")
providers_df = pd.read_csv("data/bronze/providers/providers_bronze.csv")
claims_df = pd.read_csv("data/bronze/claims/claims_bronze.csv")

claims_df = claims_df.drop_duplicates()
claims_df = claims_df[claims_df["claim_amount"] > 0]

claims_with_members = claims_df.merge(members_df, on="member_id", how="left")
claims_final = claims_with_members.merge(providers_df, on="provider_id", how="left")

claims_final = claims_final[claims_final["member_status"] == "Active"]

claims_final.to_csv("data/silver/claims_cleaned/claims_silver.csv", index=False)

print("Silver transformation completed successfully")
print(claims_final)