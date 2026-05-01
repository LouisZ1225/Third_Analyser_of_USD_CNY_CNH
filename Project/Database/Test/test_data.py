import yfinance as yf
import sqlite3
import pandas as pd

cnh = yf.download("USDCNY=X", start="2015-01-01")
print(cnh.head())
print(cnh.tail())

print(cnh.isna().sum())


def test_data(DB_PATH):
    with sqlite3.connect(DB_PATH) as conn:
        test_result = pd.read_sql_query("""
                   SELECT * FROM FX_RATES
                   ORDER BY date DESC
                   LIMIT 5
                   """,
                   conn
        )
        print(test_result)

    return 0