from typing import List, Optional
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def _get_client():
    from app.database.supabase import get_supabase
    return get_supabase()


def create_user(user_data: dict):
    client = _get_client()
    if not client:
        return user_data
    try:
        response = client.table("users").insert(user_data).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB create_user error: {e}")
        return user_data


def get_user_by_email(email: str):
    client = _get_client()
    if not client:
        return None
    try:
        response = client.table("users").select("*").eq("email", email).limit(1).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        logger.error(f"DB get_user_by_email error: {e}")
        return None


def get_user_by_id(user_id: str):
    client = _get_client()
    if not client:
        return None
    try:
        response = client.table("users").select("*").eq("id", user_id).limit(1).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        logger.error(f"DB get_user_by_id error: {e}")
        return None


def create_genome_metadata(genome_data: dict):
    client = _get_client()
    if not client:
        return genome_data
    try:
        response = client.table("genomes").insert(genome_data).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB create_genome_metadata error: {e}")
        return genome_data


def get_all_genomes():
    client = _get_client()
    if not client:
        return []
    try:
        response = client.table("genomes").select("*").order("uploaded_at", desc=True).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB get_all_genomes error: {e}")
        return []


def get_genome_by_id(genome_id: str):
    client = _get_client()
    if not client:
        return None
    try:
        response = client.table("genomes").select("*").eq("genome_id", genome_id).limit(1).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        logger.error(f"DB get_genome_by_id error: {e}")
        return None


def get_audit_logs():
    client = _get_client()
    if not client:
        return []
    try:
        response = client.table("audit_logs").select("*").order("timestamp", desc=True).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB get_audit_logs error: {e}")
        return []


def create_audit_log(log_data: dict):
    client = _get_client()
    if not client:
        return log_data
    try:
        response = client.table("audit_logs").insert(log_data).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB create_audit_log error: {e}")
        return log_data


def get_threat_alerts():
    client = _get_client()
    if not client:
        return []
    try:
        response = client.table("threat_alerts").select("*").order("created_at", desc=True).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB get_threat_alerts error: {e}")
        return []


def create_threat_alert(alert_data: dict):
    client = _get_client()
    if not client:
        return alert_data
    try:
        response = client.table("threat_alerts").insert(alert_data).execute()
        return response.data
    except Exception as e:
        logger.error(f"DB create_threat_alert error: {e}")
        return alert_data