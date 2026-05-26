from app.ai.model_selector import run_ai_analysis
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def route_ai_request(data: dict) -> str:
    logger.info(f"Routing AI request for genome: {data.get('genome_reference', 'unknown')}")
    return run_ai_analysis(data)