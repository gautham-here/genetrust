from typing import Dict, Any


def evaluate_upload_policy(file_size_bytes: int, filename: str) -> Dict[str, Any]:
    issues = []
    max_size = 100 * 1024 * 1024  # 100MB
    if file_size_bytes > max_size:
        issues.append(f"File exceeds maximum size of 100MB.")
    allowed_extensions = {".fasta", ".fa", ".fastq", ".fq", ".txt"}
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in allowed_extensions:
        issues.append(f"File extension '{ext}' is not permitted.")
    return {"allowed": len(issues) == 0, "issues": issues}


def evaluate_access_policy(user_role: str, resource: str, action: str) -> bool:
    policy_matrix = {
        "admin": ["*"],
        "researcher": ["upload", "read_own"],
        "security_analyst": ["read_all", "audit"],
        "patient": ["read_own"],
    }
    allowed = policy_matrix.get(user_role, [])
    return "*" in allowed or action in allowed or resource in allowed