from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.document import DocumentAnalysis
from app.services.document_processor import extract_document_text
from app.services.ai_service import classify_document, generate_summary


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post("/upload", response_model=DocumentAnalysis)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="A filename is required.",
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in {".pdf", ".txt", ".docx"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT, and DOCX files are supported.",
        )

    content = await file.read(MAX_FILE_SIZE + 1)

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size must not exceed 10 MB.",
        )

    document = extract_document_text(
        filename=file.filename,
        file_content=content,
    )

    text = document["text"]

    return DocumentAnalysis(
        category=classify_document(text),
        extracted_fields={
            "filename": document["filename"],
            "file_type": document["file_type"],
            "word_count": document["word_count"],
            "character_count": document["character_count"],
        },
        summary=generate_summary(text),
    )