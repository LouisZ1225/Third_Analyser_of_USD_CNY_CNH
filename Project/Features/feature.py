def calc_spread(df):
    df["spread"] = df["usd_cnh"] - df["usd_cny"]
    return df


def calc_MA(df, window=20):
    if "spread" not in df.columns:
        raise ValueError("MA requires 'spread' column")
    df[f"ma_{window}"] = df["spread"].rolling(window).mean()
    return df


def calc_volatility(df, window=20):
    if "spread" not in df.columns:
        raise ValueError("Volatility requires 'spread' column")
    df[f"vol_{window}"] = df["spread"].rolling(window).std()
    return df


def calc_diff(df, lag=1):
    if "spread" not in df.columns:
        raise ValueError("diff requires 'spread'")
    
    df[f"diff_{lag}"] = df["spread"].diff(lag)
    return df


def calc_lag(df, lag=1):
    if "spread" not in df.columns:
        raise ValueError("lag requires 'spread'")
    
    df[f"lag_{lag}"] = df["spread"].shift(lag)
    return df


def calc_zscore(df, window=20):
    if "spread" not in df.columns:
        raise ValueError("zscore requires 'spread'")
    
    mean = df["spread"].rolling(window).mean()
    std = df["spread"].rolling(window).std()
    
    df[f"zscore_{window}"] = (df["spread"] - mean) / std
    return df


FEATURE_REGISTRY = {
    "spread": calc_spread,
    "ma": calc_MA,
    "volatility": calc_volatility,
    "diff": calc_diff,
    "lag": calc_lag,
    "zscore": calc_zscore
}

def run_features(df, feature_configs):
    for f in feature_configs:
        name = f["name"]
        if name not in FEATURE_REGISTRY:
            raise ValueError(f"Unknown feature: {name}")
        func = FEATURE_REGISTRY[name]
        params = f.get("params", {})
        df = func(df, **params)
    return df