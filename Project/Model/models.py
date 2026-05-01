from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
from statsmodels.tsa.vector_ar.vecm import coint_johansen
import statsmodels.api as sm
from statsmodels.tsa.api import VAR


def run_adf(df):

    result = adfuller(df["spread"].dropna())

    print("\n===== ADF TEST =====")
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    

def run_ar(df):

    df = df.dropna()

    model = AutoReg(df["spread"], lags=1).fit()

    print("\n===== AR(1) RESULT =====")
    print(model.summary())

    return model


def run_arima(df):
    model = ARIMA(df["spread"], order=(1,0,1)).fit()
    print(model.summary())
    return model


def run_garch(df):

    df["spread"] *= 100

    returns = df["spread"].dropna()

    model = arch_model(returns, vol="Garch", p=1, q=1)
    result = model.fit()

    print("\n===== GARCH RESULT =====")
    print(result.summary())

    return result


def run_coint(df):
    result = coint_johansen(df[["usd_cny","usd_cnh"]], det_order=0, k_ar_diff=1)
    print(result.lr1)
    
    
def run_ols(df, verbose=False):
    try:
        y = df["spread"]
        X = df[["ma", "volatility"]]
        X = sm.add_constant(X)
    
        model = sm.OLS(y, X).fit()

        summary = model.summary().as_text()

        metrics = {
            "r2": model.rsquared,
            "adj_r2": model.rsquared_adj,
            "p_value": float(model.f_pvalue)
        }

        return build_result("OLS", summary, metrics)

    except Exception as e:
        return {
            "model": "OLS",
            "status": "error",
            "error": str(e)
        }
   
        
def run_var(df):

    df = df[["usd_cny", "usd_cnh"]].dropna()

    model = VAR(df)
    result = model.fit(1)

    print("\n===== VAR RESULT =====")
    print(result.summary())

    return result


def run_models(df, model_configs):
    results = {}

    for m in model_configs:
        name = m["name"]
        func = m["func"]

        try:
            result = func(df)
            results[name] = result
            print(f"✅ {name} 完成")
        except Exception as e:
            print(f"❌ {name} 失败: {e}")

    return results