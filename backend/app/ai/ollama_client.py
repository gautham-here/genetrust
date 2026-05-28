import os
import requests
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "30"))


def run_ollama(model: str, prompt: str) -> str:
    payload = {"model": model, "prompt": prompt, "stream": False}
    try:
        logger.info(f"Requesting Ollama model '{model}'.")
        response = requests.post(OLLAMA_URL, json=payload, timeout=OLLAMA_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        text = data.get("response", "").strip()
        logger.info(f"Ollama '{model}' responded ({len(text)} chars).")
        return text
    except requests.exceptions.ConnectionError:
        raise RuntimeError(f"Ollama service not reachable at {OLLAMA_URL}.")
    except Exception as e:
        logger.error(f"Ollama error: {e}")
        raise RuntimeError(f"Ollama error: {e}") from e