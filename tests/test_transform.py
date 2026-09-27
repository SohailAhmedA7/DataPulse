import pandas as pd
from etl.transform import transform_data


def test_transform_removes_duplicates():

    data = {
        "order_id": [1, 1, 2],
        "order_date": [
            "2026-01-01",
            "2026-01-01",
            "2026-01-02"
        ],
        "customer_id": [101, 101, 102],
        "customer_name": [
            " Rahul Sharma ",
            " Rahul Sharma ",
            "Priya Reddy"
        ],
        "product_id": [1, 1, 2],
        "product_name": [
            "Laptop",
            "Laptop",
            "Mouse"
        ],
        "category": [
            "Electronics",
            "Electronics",
            "Accessories"
        ],
        "quantity": [2, 2, 1],
        "unit_price": [50000, 50000, 1000],
        "revenue": [100000, 100000, 1000],
        "status": [
            "Completed",
            "Completed",
            "Completed"
        ]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert len(result) == 2


def test_revenue_calculation():

    data = {
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "customer_id": [101],
        "customer_name": ["Rahul Sharma"],
        "product_id": [1],
        "product_name": ["Laptop"],
        "category": ["Electronics"],
        "quantity": [2],
        "unit_price": [50000],
        "revenue": [0],
        "status": ["Completed"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert result.iloc[0]["revenue"] == 100000