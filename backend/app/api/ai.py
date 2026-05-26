from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.ai.model_selector import run_ai_analysis, run_ai_analysis_result
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)


class AIAnalyzePayload(BaseModel):
    genome_id: Optional[str] = None
    features: Optional[Dict[str, Any]] = None
    context: Optional[str] = None
    model: Optional[str] = None


@router.post("/ai/analyze")
def analyze(payload: AIAnalyzePayload):
    analysis_data: Dict[str, Any] = {}

    if payload.features:
        analysis_data["genomic_features"] = payload.features
    if payload.genome_id:
        analysis_data["genome_id"] = payload.genome_id
    if payload.context:
        analysis_data["context"] = payload.context

    if not analysis_data:
        raise HTTPException(status_code=400, detail="No analysis data provided.")

    logger.info(f"AI analysis request for genome: {payload.genome_id or 'unknown'}")

    try:
        result = run_ai_analysis_result(analysis_data)
        return {
            "success": True,
            "data": {
                "analysis": result.analysis,
                "genome_id": payload.genome_id,
                "ai_backend_used": result.backend_used,
                "fallback_used": result.fallback_used,
            },
            "message": "AI analysis complete.",
        }
    except Exception as e:
        logger.error(f"AI analysis error: {e}")
        raise HTTPException(status_code=503, detail=f"AI analysis failed: {str(e)}")


@router.post("/ai/analyze-raw")
def analyze_raw(payload: dict):
    try:
        result = run_ai_analysis(payload)
        return {"status": "success", "analysis": result}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
