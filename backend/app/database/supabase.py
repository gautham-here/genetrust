import os
from dotenv import load_dotenv
from app.utils.logger import setup_logger

load_dotenv()
logger = setup_logger(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

_supabase_client = None


def get_supabase():
    global _supabase_client
    if _supabase_client is not None:
        return _supabase_client
    if not SUPABASE_URL or not SUPABASE_KEY:
        logger.warning("Supabase credentials not configured. Using in-memory storage.")
        return None
    try:
        from supabase import create_client, Client
        _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        logger.info("Supabase client initialized.")
        return _supabase_client
    except Exception as e:
        logger.error(f"Supabase initialization failed: {e}")
        return None