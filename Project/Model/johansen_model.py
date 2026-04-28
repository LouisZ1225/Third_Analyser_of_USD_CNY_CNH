from statsmodels.tsa.vector_ar.vecm import coint_johansen

def run_coint(df):
    result = coint_johansen(df[["usd_cny","usd_cnh"]], det_order=0, k_ar_diff=1)
    print(result.lr1)