import os
from dataclasses import dataclass
from app.ai.gemini_client import run_gemini
from app.ai.local_inference import run_local_model
from app.ai.prompt_templates import build_risk_prompt
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


@dataclass(frozen=True)
class AIAnalysisResult:
    analysis: str
    backend_used: str
    fallback_used: bool = False


def _selected_backend() -> str:
    return os.getenv("AI_BACKEND", "gemini").strip().lower()


def _local_model_name() -> str:
    return os.getenv("LOCAL_MODEL_NAME", os.getenv("OLLAMA_MODEL", "mistral")).strip().lower()


def run_ai_analysis_result(data: dict) -> AIAnalysisResult:
    prompt = build_risk_prompt(data)
    backend = _selected_backend()
    local_model_name = _local_model_name()
    logger.info(f"AI backend selected: {backend}")

    if backend == "gemini":
        try:
            return AIAnalysisResult(
                analysis=run_gemini(prompt),
                backend_used="gemini",
            )
        except Exception as e:
            logger.warning(f"Gemini failed ({e}), falling back to Ollama model '{local_model_name}'.")
            try:
                return AIAnalysisResult(
                    analysis=run_local_model(local_model_name, prompt),
                    backend_used=f"ollama:{local_model_name}",
                    fallback_used=True,
                )
            except Exception as e2:
                logger.error(f"Ollama fallback also failed: {e2}")
                raise RuntimeError("All AI backends unavailable.") from e2

    if backend in ("ollama", "local"):
        return AIAnalysisResult(
            analysis=run_local_model(local_model_name, prompt),
            backend_used=f"ollama:{local_model_name}",
        )

    raise ValueError(f"Unknown AI_BACKEND: {backend}")


def run_ai_analysis(data: dict) -> str:
    return run_ai_analysis_result(data).analysis
