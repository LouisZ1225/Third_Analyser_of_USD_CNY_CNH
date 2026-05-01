import pandas as pd

def clean_data(df, datatype):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    
    df = df.sort_values("date")
    
    df = df[df["date"] >= "2013-07-18"]
    
    df = df.dropna(subset=["usd_cny", "usd_cnh"])
    
    df = df.set_index("date")
    
    if datatype == "fx":
        return df
    else:
        raise ValueError(f"Unsupported data type: {datatype}")