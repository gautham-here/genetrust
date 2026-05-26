from fastapi import APIRouter
from app.services.storage_service import get_all_genomes, get_genome_by_id
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)


@router.get("/genomes")
def get_genomes():
    genomes = get_all_genomes()
    return genomes


@router.get("/genomes/{genome_id}")
def get_genome(genome_id: str):
    genome = get_genome_by_id(genome_id)
    if not genome:
        return {"success": False, "data": {}, "message": f"Genome {genome_id} not found."}
    return {"success": True, "data": genome, "message": "Genome retrieved."}