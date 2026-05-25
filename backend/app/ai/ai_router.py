from app.ai.model_selector import run_ai_analysis

def route_ai_request(data: dict):
    return run_ai_analysis(data)