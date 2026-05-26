import os
import google.generativeai as genai
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

_model = None


def _get_model():
    global _model
    if _model is None:
        api_key = os.getenv("GEMINI_API_KEY", "")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        _model = genai.GenerativeModel(model_name)
        logger.info(f"Gemini model '{model_name}' initialized.")
    return _model


def run_gemini(prompt: str) -> str:
    try:
        model = _get_model()
        logger.info("Sending request to Gemini API.")
        response = model.generate_content(prompt)
        text = (getattr(response, "text", "") or "").strip()
        if not text:
            raise RuntimeError("Gemini returned an empty response.")
        logger.info(f"Gemini responded ({len(text)} chars).")
        return text
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        raise RuntimeError(f"Gemini API error: {e}") from e
