from app.ai.ollama_client import run_ollama

MODEL_NAME = "llama3"


def run_llama(prompt: str) -> str:
    return run_ollama(MODEL_NAME, prompt)