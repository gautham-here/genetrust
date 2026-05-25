from app.ai.ollama_client import run_ollama

MODEL_NAME = "phi3"

def run_phi(prompt: str):
    return run_ollama(MODEL_NAME, prompt)