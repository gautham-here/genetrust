from typing import List, Optional

from app.database.supabase import get_supabase
from app.database.models import (
    User,
    Organization,
    GenomeMetadata,
    RiskAnalysis,
    ThreatAlert,
    AuditLog,
    AccessRequest,
)

# ---------------------------------------------------
# INITIALIZE CLIENT
# ---------------------------------------------------

supabase = get_supabase()

# ---------------------------------------------------
# USER QUERIES
# ---------------------------------------------------

def create_user(user: User):

    response = (
        supabase
        .table("users")
        .insert(user.dict())
        .execute()
    )

    return response.data


def get_user_by_email(email: str):

    response = (
        supabase
        .table("users")
        .select("*")
        .eq("email", email)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


def get_user_by_id(user_id: str):

    response = (
        supabase
        .table("users")
        .select("*")
        .eq("id", user_id)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


# ---------------------------------------------------
# ORGANIZATION QUERIES
# ---------------------------------------------------

def create_organization(org: Organization):

    response = (
        supabase
        .table("organizations")
        .insert(org.dict())
        .execute()
    )

    return response.data


def get_organization(org_id: str):

    response = (
        supabase
        .table("organizations")
        .select("*")
        .eq("id", org_id)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


# ---------------------------------------------------
# GENOME QUERIES
# ---------------------------------------------------

def create_genome_metadata(
    genome: GenomeMetadata
):

    response = (
        supabase
        .table("genomes")
        .insert(genome.dict())
        .execute()
    )

    return response.data


def get_all_genomes():

    response = (
        supabase
        .table("genomes")
        .select("*")
        .order("uploaded_at", desc=True)
        .execute()
    )

    return response.data


def get_genome_by_id(genome_id: str):

    response = (
        supabase
        .table("genomes")
        .select("*")
        .eq("genome_id", genome_id)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


def get_genomes_by_owner(owner_id: str):

    response = (
        supabase
        .table("genomes")
        .select("*")
        .eq("owner_id", owner_id)
        .execute()
    )

    return response.data


# ---------------------------------------------------
# RISK ANALYSIS QUERIES
# ---------------------------------------------------

def create_risk_analysis(
    analysis: RiskAnalysis
):

    response = (
        supabase
        .table("risk_analysis")
        .insert(analysis.dict())
        .execute()
    )

    return response.data


def get_risk_analysis(
    genome_id: str
):

    response = (
        supabase
        .table("risk_analysis")
        .select("*")
        .eq("genome_id", genome_id)
        .order("generated_at", desc=True)
        .limit(1)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


# ---------------------------------------------------
# THREAT QUERIES
# ---------------------------------------------------

def create_threat_alert(
    alert: ThreatAlert
):

    response = (
        supabase
        .table("threat_alerts")
        .insert(alert.dict())
        .execute()
    )

    return response.data


def get_threat_alerts():

    response = (
        supabase
        .table("threat_alerts")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return response.data


# ---------------------------------------------------
# AUDIT LOG QUERIES
# ---------------------------------------------------

def create_audit_log(
    log: AuditLog
):

    response = (
        supabase
        .table("audit_logs")
        .insert(log.dict())
        .execute()
    )

    return response.data


def get_audit_logs():

    response = (
        supabase
        .table("audit_logs")
        .select("*")
        .order("timestamp", desc=True)
        .execute()
    )

    return response.data


# ---------------------------------------------------
# ACCESS REQUEST QUERIES
# ---------------------------------------------------

def create_access_request(
    request: AccessRequest
):

    response = (
        supabase
        .table("access_requests")
        .insert(request.dict())
        .execute()
    )

    return response.data


def get_access_requests_for_genome(
    genome_id: str
):

    response = (
        supabase
        .table("access_requests")
        .select("*")
        .eq("genome_id", genome_id)
        .order("requested_at", desc=True)
        .execute()
    )

    return response.data


def update_access_request_status(
    request_id: str,
    status: str
):

    response = (
        supabase
        .table("access_requests")
        .update({
            "status": status
        })
        .eq("id", request_id)
        .execute()
    )

    return response.data