import yfinance as yf
import pandas as pd

def fetch_fx_data(start="2010-01-01"):

    # 拉数据
    cny = yf.download("USDCNY=X", start=start)
    cnh = yf.download("USDCNH=X", start=start)

    # ✅ 去掉多层列（关键）
    cny.columns = cny.columns.get_level_values(0)
    cnh.columns = cnh.columns.get_level_values(0)

    # ✅ 统一时区（关键）
    cny.index = cny.index.tz_localize(None)
    cnh.index = cnh.index.tz_localize(None)

    # 重命名
    cny = cny[["Close"]].rename(columns={"Close": "usd_cny"})
    cnh = cnh[["Close"]].rename(columns={"Close": "usd_cnh"})

    # 用 index merge（关键）
    df = pd.concat([cny, cnh], axis=1)

    # reset index
    df = df.reset_index()
    
    df = df.rename(columns={"Date": "date"})
    # 填充缺失（关键）
    df = df.ffill()

    # 类型处理
    df["date"] = df["date"].astype(str)

    return df