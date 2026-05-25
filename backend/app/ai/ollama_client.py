import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def run_ollama(model: str, prompt: str):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        data = response.json()

        return data.get("response", "No response")

    except Exception as e:
        return f"Ollama Error: {str(e)}"