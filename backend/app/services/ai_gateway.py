from typing import Dict, Any
from app.ai.model_selector import run_ai_analysis_result
from app.genomic.anonymizer import anonymize_feature_record
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def analyze_genome_with_ai(feature_record: Dict, risk_result: Dict) -> Dict[str, Any]:
    anonymized = anonymize_feature_record(feature_record)
    analysis_payload = {
        "genomic_features": anonymized,
        "preliminary_risk": {
            "risk_score": risk_result.get("risk_score"),
            "risk_level": risk_result.get("risk_level"),
            "exposure_probability": risk_result.get("exposure_probability"),
        },
    }
    logger.info(f"Sending anonymized genome to AI pipeline: {anonymized.get('genome_reference', 'unknown')}")
    try:
        ai_response = run_ai_analysis_result(analysis_payload)
        parsed = _parse_ai_response(ai_response.analysis, risk_result)
        parsed["ai_backend_used"] = ai_response.backend_used
        parsed["ai_fallback_used"] = ai_response.fallback_used
        logger.info(f"AI analysis complete for {anonymized.get('genome_reference', 'unknown')}")
        return parsed
    except Exception as e:
        logger.error(f"AI gateway error: {e}")
        return {
            "ai_risk_level": risk_result.get("risk_level", "unknown"),
            "ai_risk_score": risk_result.get("risk_score", 0),
            "ai_summary": "AI analysis unavailable. Using heuristic risk assessment.",
            "threat_indicators": risk_result.get("findings", []),
            "privacy_concerns": ["AI service temporarily unavailable."],
            "security_recommendations": risk_result.get("recommendations", []),
            "compliance_warnings": [],
            "raw_response": "",
            "ai_backend_used": "fallback",
            "ai_fallback_used": True,
        }


def _parse_ai_response(raw: str, fallback: Dict) -> Dict[str, Any]:
    result = {
        "ai_risk_level": fallback.get("risk_level", "unknown"),
        "ai_risk_score": fallback.get("risk_score", 0),
        "ai_summary": "",
        "threat_indicators": [],
        "privacy_concerns": [],
        "security_recommendations": fallback.get("recommendations", []),
        "compliance_warnings": [],
        "raw_response": raw,
        "ai_backend_used": "unknown",
        "ai_fallback_used": False,
    }

    if not raw:
        return result

    result["ai_summary"] = raw[:500] if len(raw) > 500 else raw

    lines = raw.split("\n")
    current_section = None
    for line in lines:
        line_stripped = line.strip()
        lower = line_stripped.lower()

        if "risk assessment" in lower or "risk level" in lower:
            current_section = "risk"
        elif "threat indicator" in lower:
            current_section = "threats"
        elif "privacy concern" in lower:
            current_section = "privacy"
        elif "security recommendation" in lower or "recommendation" in lower:
            current_section = "recommendations"
        elif "compliance" in lower:
            current_section = "compliance"
        elif line_stripped.startswith(("-", "*", "\u2022", "\u00e2\u20ac\u00a2")) and current_section:
            content = line_stripped.lstrip("-* \u2022\u00e2\u20ac\u00a2").strip()
            if content:
                if current_section == "threats":
                    result["threat_indicators"].append(content)
                elif current_section == "privacy":
                    result["privacy_concerns"].append(content)
                elif current_section == "recommendations":
                    result["security_recommendations"].append(content)
                elif current_section == "compliance":
                    result["compliance_warnings"].append(content)

        for risk_word, score in [("critical", 90), ("high", 75), ("medium", 50), ("low", 25)]:
            if risk_word in lower and "risk" in lower and current_section == "risk":
                result["ai_risk_level"] = risk_word if risk_word != "medium" else "medium"
                if result["ai_risk_score"] == fallback.get("risk_score", 0):
                    result["ai_risk_score"] = score

    if not result["threat_indicators"]:
        result["threat_indicators"] = fallback.get("findings", [])
    if not result["security_recommendations"]:
        result["security_recommendations"] = fallback.get("recommendations", [])

    return result
