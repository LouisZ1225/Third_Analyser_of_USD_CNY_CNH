import requests
import json
from Report.extract_ols_result import extract_ols_metrics

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen:7b",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )
    
    full_text = ""
    
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            token = data.get("response", "")
            print(token, end="", flush=True)
            full_text += token


    return full_text
    


def generate_report(model):

    metrics = extract_ols_metrics(model)

    prompt = f"""
你是计量经济学专家，请分析以下OLS回归结果：

模型信息：

样本数: {metrics["n_obs"]}
R²: {metrics["r2"]}
Adj R²: {metrics["adj_r2"]}

变量结果：
{metrics["variables"]}

请用结构化方式输出：

1. 模型解释
2. 变量显著性
3. 经济含义
4. 模型问题（如异方差、自相关）
5. 结论
"""

    print("\n===== AI 正在生成 =====\n")

    report = ask_llm(prompt)

    return report