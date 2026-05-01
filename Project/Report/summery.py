import pandas as pd

def build_summary_table(results):
    rows = []

    for exp_name, models in results.items():
        for model_name, result in models.items():

            if result["status"] != "success":
                continue

            metrics = result.get("metrics", {})

            row = {
                "experiment": exp_name,
                "model": model_name,
                "r2": metrics.get("r2"),
                "adj_r2": metrics.get("adj_r2"),
                "p_value": metrics.get("p_value"),
                "aic": metrics.get("aic"),
                "bic": metrics.get("bic"),
                "loglik": metrics.get("loglik"),
                "adf_pvalue": metrics.get("p_value") if model_name == "ADF" else None
            }

            rows.append(row)

    df = pd.DataFrame(rows)

    return df