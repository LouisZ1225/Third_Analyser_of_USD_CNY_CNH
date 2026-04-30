def extract_ols_metrics(model):

    return {
        "n_obs": int(model.nobs),
        "r2": float(model.rsquared),
        "adj_r2": float(model.rsquared_adj),
        "f_stat": float(model.fvalue),

        "variables": [
            {
                "name": name,
                "coef": float(model.params[name]),
                "p": float(model.pvalues[name]),
                "t": float(model.tvalues[name])
            }
            for name in model.params.index
        ]
    }