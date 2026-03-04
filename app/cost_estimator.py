"""
Cost estimation and monitoring helpers for Memphis AI Platform.
Provided — no changes needed.
"""


# Real Azure Monitor metric names (from Microsoft Learn)
# Students reference these when building their monitoring plan
AZURE_MONITOR_METRICS = {
    "azure_openai": {
        "requests": "AzureOpenAIRequests",
        "prompt_tokens": "ProcessedPromptTokens",
        "generated_tokens": "GeneratedTokens",
        "total_tokens": "TokenTransaction",
        "latency": "AzureOpenAITimeToResponse",
        "availability": "AzureOpenAIAvailabilityRate",
        "content_filter": "RAIRejectedRequests",
    },
    "document_intelligence": {
        "requests": "ProcessedPages",
        "availability": "SuccessRate",
    },
    "ai_search": {
        "queries": "SearchQueriesPerSecond",
        "latency": "SearchLatency",
        "availability": "SuccessRate",
    },
    "ai_language": {
        "requests": "TextAnalyticsRequests",
        "availability": "SuccessRate",
    },
    "speech": {
        "requests": "SpeechSessionDuration",
        "availability": "SuccessRate",
    },
    "ai_vision": {
        "requests": "ComputerVisionRequests",
        "availability": "SuccessRate",
    },
}


def format_currency(amount: float) -> str:
    """Format a number as USD currency string.

    Args:
        amount: Dollar amount to format.

    Returns:
        String like "$1,234.56"
    """
    return f"${amount:,.2f}"


def get_metrics_for_service(service_key: str) -> dict:
    """Get Azure Monitor metrics for a given service.

    Args:
        service_key: Service identifier (e.g., "azure_openai", "ai_search")

    Returns:
        Dict of metric_purpose -> metric_name, or empty dict if unknown service.
    """
    return AZURE_MONITOR_METRICS.get(service_key, {})
