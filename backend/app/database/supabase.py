import os

from supabase import Client, create_client
from dotenv import load_dotenv

# ---------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ---------------------------------------------------
# VALIDATION
# ---------------------------------------------------

if not SUPABASE_URL:
    raise ValueError(
        "SUPABASE_URL environment variable is missing."
    )

if not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_KEY environment variable is missing."
    )

# ---------------------------------------------------
# CREATE CLIENT
# ---------------------------------------------------

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ---------------------------------------------------
# CONNECTION ACCESSOR
# ---------------------------------------------------

def get_supabase() -> Client:
    """
    Returns the initialized Supabase client.

    This function should be used throughout the
    application instead of creating new clients.
    """

    return supabase