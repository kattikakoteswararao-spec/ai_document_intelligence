from app.services.ai_service import (
    classify_document,
    generate_summary,
)


def test_classify_hr_document():
    text = "Employee information and Human Resources details"

    result = classify_document(text)

    assert result == "HR"


def test_classify_finance_document():
    text = "Invoice payment and budget information"

    result = classify_document(text)

    assert result == "Finance"


def test_generate_summary():
    text = "This is a sample document for testing."

    result = generate_summary(text)

    assert isinstance(result, str)
    assert len(result) > 0


def test_empty_summary():
    result = generate_summary("")

    assert result == "No text available to summarize."