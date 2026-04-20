def calc_spread(df):
    
    df["spread"] = df["usd_cnh"] - df["usd_cny"]
    
    return df