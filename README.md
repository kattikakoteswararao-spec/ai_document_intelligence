# AI Document Intelligence Pipeline

## Overview
A Python document-processing application built with FastAPI.

## Features
Upload PDF, TXT, and DOCX documents.
Extract document text and metadata.
Classify documents using keyword-based rules.
Generate document summaries.
Validate structured responses using Pydantic.
Handle unsupported files and processing errors.
Expose a REST API with Swagger documentation.

## Technologies
Python
FastAPI
Uvicorn
Pydantic
PyPDF
python-docx
Pytest

## Setup
1. Create and activate a Python virtual environment.
2. Install dependencies:

   pip install -r requirements.txt

3. Start the application:

   python -m uvicorn app.main:app --reload

4. Open Swagger UI:

   http://127.0.0.1:8000/docs

## Run Tests
   python -m pytest -v

## API Endpoint
POST /documents/upload

Upload a supported document to extract its text and return structured analysis.
