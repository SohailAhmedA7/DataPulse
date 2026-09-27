import pandas as pd


def transform_data(df):
    print("\nStarting transformation...")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Convert date column to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Clean customer names
    df["customer_name"] = df["customer_name"].str.strip()

    # Calculate revenue
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Add order month
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    print("Transformation successful!")
    print(f"Rows after transformation: {len(df)}")

    print("\nTransformed data:")
    print(df.head())

    return df


if __name__ == "__main__":
    print("Transform module is ready.")