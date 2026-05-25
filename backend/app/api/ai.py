from fastapi import APIRouter

from app.ai.model_selector import run_ai_analysis

router = APIRouter(tags=["AI"])


@router.post("/ai/analyze")
def analyze(payload: dict):

    result = run_ai_analysis(payload)

    return {
        "status": "success",
        "analysis": result
    }