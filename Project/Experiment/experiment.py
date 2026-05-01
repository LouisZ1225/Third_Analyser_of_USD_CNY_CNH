from Features.feature import run_features
from Model.models import run_models

def run_experiments(df_raw, experiments):
    results = {}

    for exp in experiments:
        name = exp["name"]
        feature_config = exp["features"]

        print(f"\n🚀 Running experiment: {name}")

        df = df_raw.copy()

        df = run_features(df, feature_config)

        model_list = exp["models"]

        model_result = run_models(df, model_list)

        results[name] = model_result

    return results