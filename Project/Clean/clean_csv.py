import pandas as pd

def load_cnh_csv(csv_path):
    df = pd.read_csv(csv_path)

    # 1️⃣ 重命名
    df = df.rename(columns={
        "Date": "date",
        "Price": "usd_cnh"
    })

    # 2️⃣ 日期格式统一
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # 3️⃣ 只保留需要的列
    df = df[["date", "usd_cnh"]]

    # 4️⃣ 排序（重要）
    df = df.sort_values("date")

    # 5️⃣ 去重
    df = df.drop_duplicates(subset="date")

    return df

def load_cny_csv(csv_path):
    df = pd.read_csv(csv_path)

    # 1️⃣ 重命名
    df = df.rename(columns={
        "Date": "date",
        "Price": "usd_cny"
    })

    # 2️⃣ 日期格式统一
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # 3️⃣ 只保留需要的列
    df = df[["date", "usd_cny"]]

    # 4️⃣ 排序（重要）
    df = df.sort_values("date")

    # 5️⃣ 去重
    df = df.drop_duplicates(subset="date")

    return df

def merge_fx_data(df_cny, df_cnh):
    df = pd.merge(df_cny, df_cnh, on="date", how="outer")

    # 排序
    df = df.sort_values("date")

    # 向前填充（关键！）
    df["usd_cny"] = df["usd_cny"].ffill()
    df["usd_cnh"] = df["usd_cnh"].ffill()

    return df