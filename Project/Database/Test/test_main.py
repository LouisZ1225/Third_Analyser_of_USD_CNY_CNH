from Fetch.fetch import fetch_fx_data

if __name__ == "__main__":
    df = fetch_fx_data()

    print("=== 前5行 ===")
    print(df.head())

    print("\n=== 后5行 ===")
    print(df.tail())

    print("\n=== 数据信息 ===")
    print(df.info())

    print("\n=== 是否有缺失值 ===")
    print(df.isna().sum())
    