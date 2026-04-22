import sqlite3
import pandas as pd

def query_rate(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM fx_daily", conn)
    conn.close()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.sort_values("date")
    df = df[df["date"] >= "2013-07-18"]
    df = df.dropna(subset=["usd_cny", "usd_cnh"])
    df = df.set_index("date")

    return df



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