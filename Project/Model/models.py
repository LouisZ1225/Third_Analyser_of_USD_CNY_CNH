from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
from statsmodels.tsa.vector_ar.vecm import coint_johansen
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from Model.models_results import build_result


def run_adf(df):
    try:
        result = adfuller(df["spread"].dropna())

        metrics = {
            "adf_stat": result[0],
            "p_value": result[1]
        }

        summary = f"ADF Statistic: {result[0]}, p-value: {result[1]}"

        return build_result("ADF", summary, metrics)

    except Exception as e:
        return {
            "model": "ADF",
            "status": "error",
            "error": str(e)
        }
    

def run_ar(df):
    try:
        df = df.dropna()

        model = AutoReg(df["spread"], lags=1).fit()

        return build_result(
            "AR",
            summary=model.summary().as_text(),
            metrics={
                "aic": model.aic,
                "bic": model.bic
            }
        )

    except Exception as e:
        return {
            "model": "AR",
            "status": "error",
            "error": str(e)
        }


def run_arima(df):
    try:
        model = ARIMA(df["spread"].dropna(), order=(1,0,1)).fit()

        return build_result(
            "ARIMA",
            summary=model.summary().as_text(),
            metrics={
                "aic": model.aic,
                "bic": model.bic
            }
        )

    except Exception as e:
        return {
            "model": "ARIMA",
            "status": "error",
            "error": str(e)
        }


def run_garch(df):
    try:
        returns = df["spread"].dropna() * 100

        model = arch_model(returns, vol="Garch", p=1, q=1)
        result = model.fit(disp="off")

        return build_result(
            "GARCH",
            summary=str(result.summary()),
            metrics={
                "loglik": result.loglikelihood
            }
        )

    except Exception as e:
        return {
            "model": "GARCH",
            "status": "error",
            "error": str(e)
        }


def run_coint(df):
    try:
        result = coint_johansen(
            df[["usd_cny", "usd_cnh"]].dropna(),
            det_order=0,
            k_ar_diff=1
        )

        trace_stat = result.lr1.tolist()

        return build_result(
            "JOHANSEN",
            summary=f"Trace stats: {trace_stat}",
            metrics={
                "trace_stat": trace_stat
            }
        )

    except Exception as e:
        return {
            "model": "JOHANSEN",
            "status": "error",
            "error": str(e)
        }
    
    
def run_ols(df):
    try:
        y = df["spread"]
        
        exclude_cols = ["spread", "usd_cny", "usd_cnh"]
        feature_cols = [col for col in df.columns if col not in exclude_cols]

        if len(feature_cols) == 0:
            raise ValueError("No feature columns available for OLS")
        
        X = df[feature_cols].dropna()
        y = y.loc[X.index]

        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        return build_result(
            "OLS",
            summary=model.summary().as_text(),
            metrics={
                "r2": model.rsquared,
                "adj_r2": model.rsquared_adj,
                "p_value": float(model.f_pvalue)
            }
        )

    except Exception as e:
        return {
            "model": "OLS",
            "status": "error",
            "error": str(e)
        }
   
        
def run_var(df):
    try:
        df = df[["usd_cny", "usd_cnh"]].dropna()

        model = VAR(df)
        result = model.fit(1)

        return build_result(
            "VAR",
            summary=result.summary().as_text(),
            metrics={
                "aic": result.aic,
                "bic": result.bic
            }
        )

    except Exception as e:
        return {
            "model": "VAR",
            "status": "error",
            "error": str(e)
        }
        

MODEL_REGISTRY = {
    "OLS": run_ols,
    "ADF": run_adf,
    "AR": run_ar,
    "ARIMA": run_arima,
    "GARCH": run_garch,
    "VAR": run_var,
    "JOHANSEN": run_coint
}


def run_models(df, model_list):
    results = {}

    for name in model_list:
        if name not in MODEL_REGISTRY:
            raise ValueError(f"Unknown model: {name}")

        func = MODEL_REGISTRY[name]

        try:
            result = func(df)
            results[name] = result
            print(f"✅ {name} 完成")
        except Exception as e:
            results[name] = {
                "model": name,
                "status": "error",
                "error": str(e)
            }
            print(f"❌ {name} 失败")

    return results