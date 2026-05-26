from app.ai.ollama_client import run_ollama

MODEL_NAME = "mistral"


def run_mistral(prompt: str) -> str:
    return run_ollama(MODEL_NAME, prompt)