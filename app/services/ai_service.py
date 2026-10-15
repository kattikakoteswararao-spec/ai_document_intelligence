def classify_document(text: str) -> str:
    """Classify a document using simple keyword rules."""

    content = text.lower()

    categories = {
        "HR": [
            "employee",
            "human resources",
            "recruitment",
            "salary",
            "leave",
        ],
        "Finance": [
            "invoice",
            "payment",
            "budget",
            "revenue",
            "tax",
        ],
        "Legal": [
            "contract",
            "agreement",
            "legal",
            "clause",
            "court",
        ],
        "Technical": [
            "python",
            "software",
            "api",
            "database",
            "system",
        ],
    }

    for category, keywords in categories.items():
        if any(keyword in content for keyword in keywords):
            return category

    return "Other"


def generate_summary(text: str) -> str:
    """Generate a basic extractive summary."""

    cleaned_text = " ".join(text.split())

    if not cleaned_text:
        return "No text available to summarize."

    words = cleaned_text.split()

    if len(words) <= 30:
        return cleaned_text

    return " ".join(words[:30]) + "..."