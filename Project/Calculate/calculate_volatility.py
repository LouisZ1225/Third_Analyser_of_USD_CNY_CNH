def calc_volatility(df, window=20):
        
    df["volatility"] = df["spread"].rolling(window).std()
    
    return df