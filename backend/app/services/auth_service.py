import uuid
import hashlib
from typing import Optional, Dict
from app.security.jwt_handler import create_access_token
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

_users: Dict[str, Dict] = {
    "admin": {
        "id": str(uuid.uuid4()),
        "username": "admin",
        "email": "admin@genetrust.io",
        "full_name": "GeneTrust Admin",
        "role": "admin",
        "password_hash": hashlib.sha256("admin123".encode()).hexdigest(),
        "is_active": True,
    },
    "researcher": {
        "id": str(uuid.uuid4()),
        "username": "researcher",
        "email": "researcher@genetrust.io",
        "full_name": "Lead Researcher",
        "role": "researcher",
        "password_hash": hashlib.sha256("research123".encode()).hexdigest(),
        "is_active": True,
    },
    "analyst": {
        "id": str(uuid.uuid4()),
        "username": "analyst",
        "email": "analyst@genetrust.io",
        "full_name": "Security Analyst",
        "role": "security_analyst",
        "password_hash": hashlib.sha256("analyst123".encode()).hexdigest(),
        "is_active": True,
    },
}


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate_user(username: str, password: str) -> Optional[Dict]:
    user = _users.get(username)
    if not user:
        logger.warning(f"Login attempt for unknown user: {username}")
        return None
    if user["password_hash"] != _hash_password(password):
        logger.warning(f"Invalid password for user: {username}")
        return None
    if not user.get("is_active", True):
        logger.warning(f"Login attempt for inactive user: {username}")
        return None
    logger.info(f"User authenticated: {username}")
    return user


def create_user_token(user: Dict) -> str:
    return create_access_token({
        "sub": user["username"],
        "role": user.get("role", "researcher"),
        "user_id": user.get("id"),
        "email": user.get("email"),
    })


def get_user_by_username(username: str) -> Optional[Dict]:
    return _users.get(username)


def register_user(username: str, email: str, password: str, full_name: str, role: str = "researcher") -> Dict:
    if username in _users:
        raise ValueError(f"Username '{username}' already exists.")
    user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "email": email,
        "full_name": full_name,
        "role": role,
        "password_hash": _hash_password(password),
        "is_active": True,
    }
    _users[username] = user
    logger.info(f"New user registered: {username} ({role})")
    return user