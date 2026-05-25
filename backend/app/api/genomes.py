from fastapi import APIRouter

router = APIRouter(tags=["Genomes"])


FAKE_GENOMES = [
    {
        "id": "GTX-1023",
        "risk": "low",
        "owner": "Research Lab A"
    },
    {
        "id": "GTX-9381",
        "risk": "high",
        "owner": "Hospital B"
    }
]


@router.get("/genomes")
def get_genomes():
    return {
        "count": len(FAKE_GENOMES),
        "genomes": FAKE_GENOMES
    }