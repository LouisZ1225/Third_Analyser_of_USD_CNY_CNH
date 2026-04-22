def calc_MA(df, window=20):
    
    df[f"ma_{window}"] = df["spread"].rolling(window).mean()
    
    return df