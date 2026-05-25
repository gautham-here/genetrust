from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# API Routers
from app.api.upload import router as upload_router

# Application Metadata
APP_NAME = "GeneTrust API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = (
    "Secure AI-native genomic identity infrastructure platform."
)

# Create FastAPI App
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)

# ---------------------------------------------------
# CORS CONFIGURATION
# ---------------------------------------------------

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# ROOT ENDPOINTS
# ---------------------------------------------------

@app.get("/", tags=["System"])
async def root():
    return {
        "platform": "GeneTrust",
        "status": "active",
        "message": (
            "Secure genomic infrastructure backend operational."
        ),
    }


@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "services": {
            "api": "online",
            "security": "active",
            "genomic_engine": "active",
        },
    }

# ---------------------------------------------------
# ROUTER REGISTRATION
# ---------------------------------------------------

app.include_router(
    upload_router,
    prefix="",
    tags=["Genome Upload"],
)