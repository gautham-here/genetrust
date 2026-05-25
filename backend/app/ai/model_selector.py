from app.ai.gemini_client import run_gemini
from app.ai.local_inference import run_local_model
from app.ai.prompt_templates import build_risk_prompt

USE_CLOUD_AI = True

def run_ai_analysis(data: dict):

    prompt = build_risk_prompt(data)

    if USE_CLOUD_AI:
        result = run_gemini(prompt)
    else:
        result = run_local_model("llama", prompt)

    return result