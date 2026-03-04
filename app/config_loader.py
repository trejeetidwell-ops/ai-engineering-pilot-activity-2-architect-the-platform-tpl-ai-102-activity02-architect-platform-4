"""
Multi-service configuration loader for Memphis AI Platform.
Provided — no changes needed.
"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class ServiceConfig:
    """Configuration for a single Azure AI service."""
    name: str
    endpoint_var: str
    key_var: str
    endpoint: str = ""
    key: str = ""
    loaded: bool = False


REQUIRED_SERVICES = [
    ServiceConfig(name="Azure OpenAI", endpoint_var="AZURE_OPENAI_ENDPOINT", key_var="AZURE_OPENAI_API_KEY"),
    ServiceConfig(name="Azure AI Search", endpoint_var="AZURE_AI_SEARCH_ENDPOINT", key_var="AZURE_AI_SEARCH_KEY"),
    ServiceConfig(name="Azure Document Intelligence", endpoint_var="AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT", key_var="AZURE_DOCUMENT_INTELLIGENCE_KEY"),
    ServiceConfig(name="Azure AI Language", endpoint_var="AZURE_AI_LANGUAGE_ENDPOINT", key_var="AZURE_AI_LANGUAGE_KEY"),
]


def load_all_configs() -> list[ServiceConfig]:
    """Load environment variables for all required services.

    Returns:
        List of ServiceConfig with endpoint/key filled from env vars.
    """
    load_dotenv()
    configs = []
    for svc in REQUIRED_SERVICES:
        config = ServiceConfig(
            name=svc.name,
            endpoint_var=svc.endpoint_var,
            key_var=svc.key_var,
            endpoint=os.getenv(svc.endpoint_var, ""),
            key=os.getenv(svc.key_var, ""),
        )
        config.loaded = bool(config.endpoint and config.key)
        configs.append(config)
    return configs
