import pandas as pd

try:

    print("=" * 60)
    print("HEALTHCARE CLAIMS DATA VALIDATION REPORT")
    print("=" * 60)

    # Read Files
    raw_claims = pd.read_csv("data/raw/claims.csv")
    silver_claims = pd.read_csv("data/silver/claims_cleaned/claims_silver.csv")

    # --------------------------------------------------
    # Debugging
    # --------------------------------------------------

    print("\nDEBUG - RAW DATA")
    print(raw_claims.head())

    print("\nDEBUG - SILVER DATA")
    print(silver_claims.head())

    print("\nDEBUG - SILVER COLUMNS")
    print(silver_claims.columns.tolist())

    print("\nDEBUG - SILVER SHAPE")
    print(silver_claims.shape)

    # --------------------------------------------------
    # Target Not Empty Validation
    # --------------------------------------------------

    assert len(silver_claims) > 0, "Target file is empty"

    print("\n✓ Target file contains records")

    # --------------------------------------------------
    # Record Count Validation
    # --------------------------------------------------

    source_count = len(raw_claims)
    target_count = len(silver_claims)

    print("\n1. RECORD COUNT VALIDATION")
    print("Source Count :", source_count)
    print("Target Count :", target_count)

    # --------------------------------------------------
    # Null Validation
    # --------------------------------------------------

    print("\n2. NULL VALIDATION")

    null_counts = silver_claims.isnull().sum()

    print(null_counts)

    claim_id_nulls = silver_claims["claim_id"].isnull().sum()

    assert claim_id_nulls == 0, "claim_id contains NULL values"

    print("✓ claim_id NULL validation passed")

    # --------------------------------------------------
    # Duplicate Validation
    # --------------------------------------------------

    print("\n3. DUPLICATE VALIDATION")

    duplicate_count = silver_claims.duplicated(
        subset=["member_id", "claim_id"]
    ).sum()

    print("Duplicate Records :", duplicate_count)

    assert duplicate_count == 0, "Duplicate records found"

    print("✓ Duplicate validation passed")

    # --------------------------------------------------
    # Invalid Claim Amount Validation
    # --------------------------------------------------

    print("\n4. CLAIM AMOUNT VALIDATION")

    invalid_claims = silver_claims[
        silver_claims["claim_amount"] <= 0
    ]

    print("Invalid Claims :", len(invalid_claims))

    assert len(invalid_claims) == 0, \
        "Claim amount should be greater than zero"

    print("✓ Claim amount validation passed")

    # --------------------------------------------------
    # Paid Amount Validation
    # --------------------------------------------------
    print("\nPAID AMOUNT VALIDATION")

    invalid_paid = silver_claims[
    silver_claims["amount_paid"] >
    silver_claims["claim_amount"]
    ]

    print(
    "Invalid Paid Amount Records :",
    len(invalid_paid)
   )

    assert len(invalid_paid) == 0, \
    "Paid amount exceeds claim amount"

    print("✓ Paid amount validation passed")

    # --------------------------------------------------
    # Missing Record Validation
    # --------------------------------------------------

    print("\n5. MISSING RECORD VALIDATION")

    missing_df = raw_claims[
        ~raw_claims["claim_id"].isin(
            silver_claims["claim_id"]
        )
    ]

    print("Missing Records :", len(missing_df))

    if len(missing_df) > 0:
        print("\nMissing Records Sample:")
        print(missing_df)

    # --------------------------------------------------
    # Active Member Validation
    # --------------------------------------------------

    print("\n6. ACTIVE MEMBER VALIDATION")

    if "member_status" in silver_claims.columns:

        inactive_members = silver_claims[
            silver_claims["member_status"] != "Active"
        ]

        print(
            "Inactive Members :",
            len(inactive_members)
        )

        assert len(inactive_members) == 0, \
            "Inactive members found"

        print("✓ Active member validation passed")

    else:
        print("member_status column not found")

    # --------------------------------------------------
    # Unique Member Validation
    # --------------------------------------------------

    print("\n7. UNIQUE MEMBER VALIDATION")

    unique_members = silver_claims[
        "member_id"
    ].nunique()

    print("Unique Members :", unique_members)

    # --------------------------------------------------
    # Claim Amount Summary
    # --------------------------------------------------

    print("\n8. CLAIM AMOUNT SUMMARY")

    total_claim_amount = silver_claims[
        "claim_amount"
    ].sum()

    print(
        "Total Claim Amount :",
        total_claim_amount
    )

    # --------------------------------------------------
    # Final Status
    # --------------------------------------------------

    print("\n9. FINAL STATUS")

    print("VALIDATION STATUS : PASS")

    print("\nValidation Completed Successfully")

except AssertionError as e:

    print("\nVALIDATION FAILED")
    print(f"Reason : {e}")

    raise

except Exception as e:

    print("\nUNEXPECTED ERROR")
    print(f"Reason : {e}")

    raise

finally:

    print("\nValidation Execution Finished")


    print("=" * 60)
