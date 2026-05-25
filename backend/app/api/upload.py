from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid

from app.genomic.parser import parse_fasta
from app.services.risk_engine import generate_risk_analysis

router = APIRouter(tags=["Upload"])

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-genome")
async def upload_genome(file: UploadFile = File(...)):

    if not file.filename.endswith((".fasta", ".fa", ".txt")):
        raise HTTPException(
            status_code=400,
            detail="Only FASTA files are supported"
        )

    file_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}_{file.filename}"
    )

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    parsed_data = parse_fasta(file_path)

    risk_analysis = generate_risk_analysis(
        parsed_data,
        []
    )

    return {
        "genome_id": f"GTX-{file_id[:6]}",
        "filename": file.filename,
        "status": "uploaded",
        "parsed_data": parsed_data,
        "risk_analysis": risk_analysis
    }