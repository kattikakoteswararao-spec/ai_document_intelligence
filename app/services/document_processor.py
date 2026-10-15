from io import BytesIO
from pathlib import Path

from docx import Document
from fastapi import HTTPException
from pypdf import PdfReader


def extract_document_text(
    filename: str,
    file_content: bytes,
) -> dict:
    """
    Extract text and basic metadata from PDF, TXT, and DOCX files.
    """

    extension = Path(filename).suffix.lower()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty.",
        )

    try:
        if extension == ".txt":
            text = file_content.decode("utf-8-sig")

        elif extension == ".pdf":
            reader = PdfReader(BytesIO(file_content))

            if reader.is_encrypted:
                raise HTTPException(
                    status_code=400,
                    detail="Encrypted PDF files are not supported.",
                )

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        elif extension == ".docx":
            document = Document(BytesIO(file_content))

            paragraphs = [
                paragraph.text
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            ]

            text = "\n".join(paragraphs)

        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type. Upload PDF, TXT, or DOCX.",
            )

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text was found in the document.",
            )

        return {
            "filename": Path(filename).name,
            "file_type": extension.lstrip("."),
            "character_count": len(text),
            "word_count": len(text.split()),
            "text": text,
        }

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Could not process the document: {exc}",
        ) from exc