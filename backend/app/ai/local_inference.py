from app.ai.llama_client import run_llama
from app.ai.mistral_client import run_mistral
from app.ai.phi_client import run_phi

LOCAL_MODELS = {
    "llama": run_llama,
    "mistral": run_mistral,
    "phi": run_phi
}

def run_local_model(model: str, prompt: str):

    if model not in LOCAL_MODELS:
        return "Invalid local model"

    return LOCAL_MODELS[model](prompt)