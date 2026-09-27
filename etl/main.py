from extract import extract_orders
from transform import transform_data
from load import load_data


def run_pipeline():
    print("\n==============================")
    print("   DATAPULSE ETL PIPELINE")
    print("==============================")

    # 1. Extract
    df = extract_orders()

    # 2. Transform
    df = transform_data(df)

    # 3. Load
    load_data(df)

    print("\n==============================")
    print("   ETL PIPELINE COMPLETED")
    print("==============================")


if __name__ == "__main__":
    run_pipeline()