# DataPulse – Analytics Platform

DataPulse is an end-to-end data analytics platform designed to transform raw sales data into meaningful business insights.

## 🚀 Project Overview

The project implements a complete data pipeline:

**Extract → Transform → Load → Analyze → Visualize**

It includes data extraction, transformation, database loading, SQL analytics, automated testing, and an interactive Streamlit dashboard.

## ✨ Key Features

- Automated ETL pipeline
- Data cleaning and transformation
- SQL-based analytics
- Customer and sales analysis
- Interactive Streamlit dashboard
- KPI monitoring
- Category and status filters
- Automated unit tests
- Modular project structure

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **SQL**
- **SQLite**
- **SQLAlchemy**
- **Streamlit**
- **Pytest**
- **Git & GitHub**

## 📂 Project Structure

```text
DataPulse/
│
├── backend/
│   ├── dashboards/
│   │   └── dashboard.py
│   │
│   └── database/
│       ├── analytics.sql
│       ├── business_schema.sql
│       └── schema.sql
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   └── __init__.py
│
├── tests/
│   └── test_transform.py
│
├── requirements.txt
├── .gitignore
└── README.md