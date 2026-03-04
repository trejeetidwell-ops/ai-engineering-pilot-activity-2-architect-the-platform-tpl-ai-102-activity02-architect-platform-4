"""Azure AI service catalog for Activity 2. No changes needed.

This module provides a read-only catalog of Azure AI services with their
capabilities, SDK packages, models, use cases, and responsible AI considerations.
Use this catalog to match city department scenarios to the best-fit service.
"""

AZURE_AI_SERVICES = {
    "azure_openai": {
        "display_name": "Azure OpenAI Service",
        "capabilities": [
            "text_generation",
            "classification",
            "summarization",
            "chat",
            "image_classification",
            "pii_redaction",
            "form_extraction",
        ],
        "sdk": "openai",
        "models": ["gpt-4o", "gpt-4o-mini"],
        "use_cases": ["NLP classification", "content generation"],
        "responsible_ai": [
            "content filtering",
            "prompt injection risk",
            "bias monitoring",
        ],
    },
    "document_intelligence": {
        "display_name": "Azure Document Intelligence",
        "capabilities": [
            "form_extraction",
            "ocr",
            "layout_analysis",
            "handwriting_recognition",
        ],
        "sdk": "azure-ai-formrecognizer",
        "models": ["prebuilt-layout", "prebuilt-document"],
        "use_cases": ["form digitization", "invoice processing"],
        "responsible_ai": [
            "PII in extracted data",
            "data retention policies",
        ],
    },
    "ai_search": {
        "display_name": "Azure AI Search",
        "capabilities": [
            "full_text_search",
            "vector_search",
            "semantic_ranking",
            "faceted_navigation",
        ],
        "sdk": "azure-search-documents",
        "models": ["semantic_ranker"],
        "use_cases": ["document search", "knowledge mining"],
        "responsible_ai": [
            "search result bias",
            "content filtering in results",
        ],
    },
    "ai_language": {
        "display_name": "Azure AI Language",
        "capabilities": [
            "entity_recognition",
            "pii_detection",
            "pii_redaction",
            "sentiment_analysis",
            "key_phrase_extraction",
            "classification",
        ],
        "sdk": "azure-ai-textanalytics",
        "models": ["text-analytics-model"],
        "use_cases": ["PII redaction", "text analytics"],
        "responsible_ai": [
            "PII handling policies",
            "consent requirements",
        ],
    },
    "speech": {
        "display_name": "Azure Speech Services",
        "capabilities": [
            "speech_to_text",
            "text_to_speech",
            "translation",
            "real_time_transcription",
        ],
        "sdk": "azure-cognitiveservices-speech",
        "models": ["whisper", "neural-tts"],
        "use_cases": ["transcription", "translation", "accessibility"],
        "responsible_ai": [
            "voice consent",
            "deepfake prevention",
            "accent bias",
        ],
    },
    "ai_vision": {
        "display_name": "Azure AI Vision",
        "capabilities": [
            "image_classification",
            "object_detection",
            "image_analysis",
            "spatial_analysis",
        ],
        "sdk": "azure-ai-vision",
        "models": ["florence", "custom-vision"],
        "use_cases": ["image classification", "defect detection"],
        "responsible_ai": [
            "surveillance concerns",
            "demographic bias in recognition",
        ],
    },
    "content_safety": {
        "display_name": "Azure Content Safety",
        "capabilities": [
            "text_moderation",
            "image_moderation",
            "prompt_shield",
        ],
        "sdk": "azure-ai-contentsafety",
        "models": ["content-safety-model"],
        "use_cases": ["content moderation", "prompt injection defense"],
        "responsible_ai": [
            "over-blocking risk",
            "cultural context",
        ],
    },
}


def get_service_by_capability(capability: str) -> list[str]:
    """Return service names whose capabilities list includes the given capability.

    Args:
        capability: A capability string (e.g., "classification", "pii_redaction").

    Returns:
        A list of service key names that support the capability.

    Example:
        >>> get_service_by_capability("pii_redaction")
        ['azure_openai', 'ai_language']
    """
    return [
        name
        for name, info in AZURE_AI_SERVICES.items()
        if capability in info["capabilities"]
    ]
