import pandas as pd
import os

print("Gold Layer Started")

os.makedirs("data/gold/claim_summary", exist_ok=True)

claims_df = pd.read_csv("data/silver/claims_cleaned/claims_silver.csv")

print("Available columns:")
print(claims_df.columns)

# In silver file, member state usually becomes state_x and provider state becomes state_y
if "state" in claims_df.columns:
    state_column = "state"
elif "state_x" in claims_df.columns:
    state_column = "state_x"
elif "state_member" in claims_df.columns:
    state_column = "state_member"
else:
    raise Exception("State column not found in silver file")

summary_df = claims_df.groupby(
    [state_column, "claim_status"]
)["claim_amount"].sum().reset_index()

summary_df.rename(
    columns={
        state_column: "member_state",
        "claim_amount": "total_claim_amount"
    },
    inplace=True
)

summary_df.to_csv(
    "data/gold/claim_summary/claim_summary.csv",
    index=False
)

print(summary_df)
print("Gold Layer Completed Successfully")