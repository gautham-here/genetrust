import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.genomic.parser import parse_fasta_bytes
from app.genomic.feature_extractor import extract_genomic_features
from app.genomic.mutation_detector import analyze_mutation_signatures
from app.services.risk_engine import generate_risk_analysis
from app.services.ai_gateway import analyze_genome_with_ai
from app.services.storage_service import save_genome_file, encrypt_and_store, register_genome
from app.services.threat_engine import evaluate_genome_threats
from app.services.audit_service import log_event
from app.utils.logger import setup_logger

router = APIRouter()
logger = setup_logger(__name__)

ALLOWED_EXTENSIONS = {".fasta", ".fa", ".fastq", ".fq", ".txt"}


@router.post("/upload-genome")
async def upload_genome(file: UploadFile = File(...)):
    filename = file.filename or "upload"
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only FASTA/FASTQ files are supported (.fasta, .fa, .fastq, .fq).")

    content = await file.read()
    if len(content) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    file_id = str(uuid.uuid4())
    genome_id = f"GTX-{file_id[:6].upper()}"

    logger.info(f"Processing upload: {filename} → {genome_id}")

    try:
        parsed_data = parse_fasta_bytes(content, filename)
    except Exception as e:
        logger.error(f"Parse error for {filename}: {e}")
        raise HTTPException(status_code=422, detail=f"Genomic file parse error: {str(e)}")

    if not parsed_data:
        raise HTTPException(status_code=422, detail="No valid genomic sequences found in uploaded file.")

    file_path = save_genome_file(content, filename)

    encrypted_path = ""
    try:
        encrypted_path = encrypt_and_store(content, genome_id)
    except Exception as e:
        logger.warning(f"Encryption failed (non-fatal): {e}")

    feature_records = extract_genomic_features(parsed_data)
    mutation_reports = analyze_mutation_signatures(feature_records)
    risk_analysis = generate_risk_analysis(feature_records, mutation_reports)

    ai_results = []
    for feat, risk in zip(feature_records, risk_analysis):
        try:
            ai_result = analyze_genome_with_ai(feat, risk)
            ai_results.append(ai_result)
        except Exception as e:
            logger.warning(f"AI analysis failed for {feat.get('genome_label')}: {e}")
            ai_results.append({
                "ai_risk_level": risk.get("risk_level"),
                "ai_risk_score": risk.get("risk_score"),
                "ai_summary": "AI analysis unavailable. Heuristic risk assessment applied.",
                "threat_indicators": risk.get("findings", []),
                "privacy_concerns": [],
                "security_recommendations": risk.get("recommendations", []),
                "compliance_warnings": [],
                "raw_response": "",
                "ai_backend_used": "fallback",
            })

    primary = risk_analysis[0] if risk_analysis else {}
    primary_feature = feature_records[0] if feature_records else {}
    primary_parsed = parsed_data[0] if parsed_data else {}

    register_genome(
        genome_id=genome_id,
        filename=filename,
        gc_content=primary_parsed.get("gc_content", 0.0),
        genome_length=primary_parsed.get("sequence_length", 0),
        risk_level=primary.get("risk_level", "unknown"),
        risk_score=primary.get("risk_score", 0),
        encrypted_path=encrypted_path,
    )

    evaluate_genome_threats(primary, genome_id)

    log_event(
        action="Genome Upload & AI Analysis",
        user="upload_pipeline",
        genome_id=genome_id,
        severity="Low" if primary.get("risk_level") == "low" else
                  "Medium" if primary.get("risk_level") == "medium" else "High",
        status="success",
        metadata={"filename": filename, "risk_score": primary.get("risk_score", 0)},
    )

    enriched_risk = []
    for r, ai in zip(risk_analysis, ai_results):
        enriched_risk.append({
            **r,
            "ai_analysis": ai,
        })

    return {
        "genome_id": genome_id,
        "filename": filename,
        "status": "uploaded",
        "parsed_data": parsed_data,
        "risk_analysis": enriched_risk,
    }