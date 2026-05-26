from typing import Callable, Dict
from app.ai.llama_client import run_llama
from app.ai.mistral_client import run_mistral
from app.ai.phi_client import run_phi
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

LOCAL_MODELS: Dict[str, Callable[[str], str]] = {
    "llama": run_llama,
    "llama3": run_llama,
    "mistral": run_mistral,
    "phi": run_phi,
    "phi3": run_phi,
}


def run_local_model(model: str, prompt: str) -> str:
    if model not in LOCAL_MODELS:
        raise ValueError(f"Unknown local model: {model}. Available: {list(LOCAL_MODELS.keys())}")
    logger.info(f"Running local model: {model}")
    return LOCAL_MODELS[model](prompt)