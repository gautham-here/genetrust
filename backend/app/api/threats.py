from fastapi import APIRouter

router = APIRouter(tags=["Threats"])


THREATS = [
    {
        "severity": "high",
        "message": "Unauthorized genomic export attempt detected"
    },
    {
        "severity": "medium",
        "message": "Suspicious AI inference access"
    }
]


@router.get("/threats")
def get_threats():

    return {
        "alerts": THREATS,
        "count": len(THREATS)
    }