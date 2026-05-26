from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.services.audit_service import log_event
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

AUDITED_PATHS = {"/upload-genome", "/ai/analyze", "/auth/login"}


class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if request.url.path in AUDITED_PATHS and request.method == "POST":
            status = "success" if response.status_code < 400 else "failed"
            log_event(
                action=f"API {request.method} {request.url.path}",
                user=request.headers.get("X-User", "anonymous"),
                severity="Low",
                status=status,
            )
        return response