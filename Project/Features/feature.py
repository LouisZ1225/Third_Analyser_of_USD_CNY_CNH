def calc_MA(df, window=20):
    
    df[f"ma_{window}"] = df["spread"].rolling(window).mean()
    
    return df


def calc_spread(df):
    
    df["spread"] = df["usd_cnh"] - df["usd_cny"]
    
    return df


def calc_volatility(df, window=20):
        
    df["volatility"] = df["spread"].rolling(window).std()
    
    return df


def run_features(df, feature_configs):
    for f in feature_configs:
        df = f["func"](df, **f["params"])
    return df