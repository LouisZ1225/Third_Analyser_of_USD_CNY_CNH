import yfinance as yf

cnh = yf.download("USDCNY=X", start="2015-01-01")
print(cnh.head())
print(cnh.tail())

print(cnh.isna().sum())