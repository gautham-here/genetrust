from app.blockchain.chain_service import (
    get_chain_service
)

from app.utils.logger import (
    setup_logger
)

logger = setup_logger(__name__)


def register_genome_on_chain(
    anonymized_sequence: str,
    sample_id: str,
):

    try:

        svc = get_chain_service()

        result = svc.register_genome(

            anonymized_sequence,

            sample_id,
        )

        return result

    except Exception as e:

        logger.error(
            f"Blockchain registration failed: {e}"
        )

        return None