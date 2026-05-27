import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import time
from app.utils.logger import setup_logger
from app.api import upload, genomes, auth, ai, audit, threats, organizations, permissions

logger = setup_logger(__name__)

APP_NAME = "GeneTrust API"
APP_VERSION = "2.0.0"
APP_DESCRIPTION = "AI-Native Genomic CyberBioSecurity Infrastructure."

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)


from app.blockchain.routes import router as blockchain_router
app.include_router(blockchain_router, prefix="/api/v1/chain")

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = round((time.time() - start) * 1000, 2)
    logger.info(f"{request.method} {request.url.path} → {response.status_code} ({duration}ms)")
    return response


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception on {request.url.path}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"success": False, "data": {}, "message": "Internal server error."},
    )


@app.get("/", tags=["System"])
async def root():
    return {
        "success": True,
        "data": {"platform": "GeneTrust", "version": APP_VERSION},
        "message": "Secure genomic infrastructure backend operational.",
    }


@app.get("/health", tags=["System"])
async def health_check():
    return {
        "success": True,
        "data": {
            "status": "healthy",
            "services": {
                "api": "online",
                "security": "active",
                "genomic_engine": "active",
                "ai_pipeline": "active",
            },
        },
        "message": "All systems operational.",
    }


app.include_router(upload.router, tags=["Upload"])
app.include_router(genomes.router, tags=["Genomes"])
app.include_router(auth.router, tags=["Auth"])
app.include_router(ai.router, tags=["AI"])
app.include_router(audit.router, tags=["Audit"])
app.include_router(threats.router, tags=["Threats"])
app.include_router(organizations.router, tags=["Organizations"])
app.include_router(permissions.router, tags=["Permissions"])