def build_result(model_name, summary=None, metrics=None, series=None):
    return {
        "model": model_name,
        "status": "success",
        "summary": summary,
        "metrics": metrics or {},
        "series": series or {}
    }