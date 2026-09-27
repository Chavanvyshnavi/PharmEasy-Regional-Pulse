import pandas as pd
# 1. Load the raw data

df = pd.read_csv("pharmeasy_orders_raw.csv")

print("Raw rows:", len(df))
# 2. Remove exact duplicate rows

before_duplicates = len(df)

df = df.drop_duplicates()

duplicates_removed = before_duplicates - len(df)

print("Exact duplicate rows removed:", duplicates_removed)
print("Rows after removing duplicates:", len(df))


df["region"] = df["region"].astype(str).str.strip().str.title()

print("Region names normalized.")

product_category_lookup = (
    df.dropna(subset=["category"])
      .drop_duplicates(subset=["product"])
      .set_index("product")["category"]
      .to_dict()
)

# Fill missing category using product name

df["category"] = df["category"].fillna(
    df["product"].map(product_category_lookup)
)

print("Missing category values after imputation:",
      df["category"].isna().sum())

# Impute missing profit

# Convert profit and sales to numeric

df["profit_inr"] = pd.to_numeric(df["profit_inr"], errors="coerce")
df["sales_inr"] = pd.to_numeric(df["sales_inr"], errors="coerce")

df["profit_margin"] = df["profit_inr"] / df["sales_inr"]


category_mean_margin = (
    df.dropna(subset=["profit_margin"])
      .groupby("category")["profit_margin"]
      .mean()
      .to_dict()
)

missing_profit = df["profit_inr"].isna()

df.loc[missing_profit, "profit_inr"] = (
    df.loc[missing_profit, "sales_inr"]
      * df.loc[missing_profit, "category"]
        .map(category_mean_margin)
).round(2)

df.drop(columns=["profit_margin"], inplace=True)

print("Missing profit values after imputation:",
      df["profit_inr"].isna().sum())


df.to_csv("orders_clean.csv", index=False)

print("\nCleaned dataset saved as orders_clean.csv")
print("Final rows:", len(df))

def validate_schema(df, required_columns):

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        status = "blocked_schema"
    else:
        status = "validated"

    return {
        "status": status,
        "row_count": len(df),
        "missing_columns": missing_columns
    }

# 8. Validate the cleaned dataset

required_columns = [
    "order_id",
    "order_date",
    "region",
    "category",
    "product",
    "quantity",
    "sales_inr",
    "profit_inr"
]

validation_result = validate_schema(df, required_columns)

print("\nClean data validation:")
print(validation_result)

# 9. Test blocked_schema path

broken_df = df.drop(columns=["profit_inr"])

broken_validation = validate_schema(
    broken_df,
    required_columns
)

print("\nBroken data validation:")
print(broken_validation)