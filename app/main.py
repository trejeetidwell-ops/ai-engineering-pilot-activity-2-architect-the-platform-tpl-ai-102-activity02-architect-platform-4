"""
Activity 2 - Architect the Platform
AI-102: Plan, manage, and secure an Azure AI solution

Your task:
  1. Build architecture decisions for 6 Memphis departments
  2. Build shared resource configuration (resource group, auth, networking)
  3. Estimate monthly costs and check department budgets
  4. Build a monitoring plan targeting over-budget departments
  5. Assemble final outputs: design.json + result.json

Output:
  - design.json — architecture design (service selections, shared resources)
  - result.json — services_configured, security_audit, cost_estimates,
    total_monthly_cost_usd, departments_over_budget, monitoring_plan
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services import AZURE_AI_SERVICES, get_service_by_capability
from config_loader import load_all_configs, REQUIRED_SERVICES
from cost_estimator import AZURE_MONITOR_METRICS, format_currency, get_metrics_for_service
from utils import write_design, write_result


# ─── Data loaders ────────────────────────────────────────────────────────────

def load_scenarios(path=None):
    """Load city department scenarios from JSON file."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data", "city_scenarios.json")
    with open(path) as f:
        return json.load(f)


def load_pricing(path=None):
    """Load the pricing catalog from JSON."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data", "pricing_catalog.json")
    with open(path) as f:
        return json.load(f)


def load_usage(path=None):
    """Load the usage scenarios from JSON."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data", "usage_scenarios.json")
    with open(path) as f:
        return json.load(f)


# ─── Part A: Architecture Decisions ──────────────────────────────────────────

def find_services(scenarios):
    """Find the services that match the capability needed in each department's scenario.

    Returns a dict mapping department name (str) to a list of valid service
    key strings, e.g. ``{'311 Call Center': ['azure_openai', 'ai_language'], ...}``.

    When implemented successfully, this will show the available services for
    each department's need when you run main.py.

    Args:
        scenarios: a list of scenario dicts from data/city_scenarios.json

    Returns:
        dict mapping department name to list of matching service keys
    """
    # TODO: Implement this function to iterate through the scenarios dict and find available services
    # Find the specifications for the scenarios and services in the README
    # Use get_service_by_capability() to find appropriate services for each scenario

    return {}

def build_architecture_decisions() -> list:
    """Return your architecture decisions for all 6 Memphis departments.

    Each dict must have these keys:
        department, primary_service, model_or_tier, sdk_package,
        justification, alternative_considered, why_not_alternative,
        responsible_ai_considerations

    The first entry (311 Call Center) is provided as an example.
    Fill in the remaining 5 departments by reading data/city_scenarios.json
    and app/services.py.
    """
    # TODO: Fill in the remaining 5 department decisions.
    # Read each department's pain_point and constraints in data/city_scenarios.json.
    # Use get_service_by_capability() or read services.py to find candidate services.
    # Pick the best service, look up its sdk and models in AZURE_AI_SERVICES,
    # and write a unique justification (at least 20 words) for each department.
    decisions = [
        # EXAMPLE — 311 Call Center (do not modify)
        {
            "department": "311 Call Center",
            "primary_service": "azure_openai",
            "model_or_tier": "gpt-4o",
            "sdk_package": "openai",
            "justification": (
                "The 311 Call Center needs to classify free-text citizen complaints "
                "into categories. GPT-4o excels at open-ended text classification "
                "because it can interpret varied phrasings without predefined rules. "
                "AI Language's classification requires a trained model with labeled "
                "examples, which is less flexible for the wide variety of 311 inputs."
            ),
            "alternative_considered": "ai_language",
            "why_not_alternative": (
                "AI Language offers built-in classification but requires a custom "
                "trained model with labeled training data for each category."
            ),
            "responsible_ai_considerations": [
                "content filtering",
                "bias monitoring",
            ],
        },
        # TODO: Public Works — read data/city_scenarios.json and app/services.py
        {},
        # TODO: Parks & Recreation
        {},
        # TODO: Police (Community Relations)
        {},
        # TODO: Mayor's Office
        {},
        # TODO: Code Enforcement
        {},
    ]
    return decisions


def build_shared_resources() -> dict:
    """Build the shared resources configuration for the Memphis AI platform.

    Returns:
        dict with keys: resource_group, auth_model, networking
    """
    # TODO: Return a shared resources configuration
    # - resource_group: a resource group name following Azure naming conventions
    # - auth_model: explain your chosen authentication approach (mention at least
    #   one of: key-based, RBAC, or managed identity)
    # - networking: explain your network security approach
    return {}

# ─── Part B: Cost Estimation ─────────────────────────────────────────────────

def estimate_cost(usage_item: dict, pricing: dict) -> dict:
    """Estimate the monthly cost for a single department's usage.

    Args:
        usage_item: Dict with keys: department, service, monthly_volume, unit, budget_threshold_usd
        pricing: The full pricing catalog dict

    Returns:
        dict with keys: department, service, monthly_volume, unit,
        unit_cost_usd, monthly_cost_usd, within_budget, budget_threshold_usd
    """
    # TODO: Implement cost estimation
    # 1. Look up the unit_cost for this service in the pricing catalog
    # 2. Calculate: monthly_cost = monthly_volume * unit_cost
    # 3. Compare monthly_cost to budget_threshold_usd
    # 4. Return a dict with all required fields
    return {}


def check_budget(estimates: list) -> list:
    """Identify departments that exceed their budget threshold.

    Args:
        estimates: List of cost estimate dicts from estimate_cost()

    Returns:
        List of department names that are over budget
    """
    # TODO: Find departments where within_budget is False
    return []


# ─── Part B (cont.): Monitoring Plan ─────────────────────────────────────────

def build_monitoring_plan(estimates: list, over_budget: list) -> dict:
    """Build a monitoring plan targeting over-budget departments.

    Args:
        estimates: List of cost estimate dicts from estimate_cost()
        over_budget: List of department names that exceeded their budget

    Returns:
        dict with keys:
        - metrics_to_track: list of dicts with metric, service, purpose
          (at least 3 metrics)
        - alert_rules: list of dicts with department, condition, action
          (at least 1 alert rule per over-budget department)
    """
    # TODO: Build a monitoring plan
    # 1. Select at least 3 metrics from AZURE_MONITOR_METRICS to track
    #    - Use get_metrics_for_service() to look up metrics by service
    #    - Each metric dict needs: metric, service, purpose
    # 2. Write at least 1 alert rule for EACH over-budget department
    #    - Use the estimates list to find which service each department uses
    #    - Use get_metrics_for_service() to find valid metric names for that service
    #    - Each alert rule needs: department, condition (metric + threshold), action
    # 3. Use the real metric names from cost_estimator.py — do not make up names
    return {}

# ─── Reference: Config Validation & Security Audit ─────────────────────────────

def validate_service_config(service_name: str, endpoint: str, key: str) -> dict:
    """Validate a single service's configuration.

    Args:
        service_name: Name of the Azure service
        endpoint: The service endpoint URL to validate
        key: The API key string

    Returns:
        dict with keys: service_name, endpoint_valid, key_present, endpoint_pattern
    """
    # TODO: Write a regex pattern that matches valid Azure AI endpoint URLs.
    # Azure endpoints use three domain suffixes:
    #   - openai.azure.com         (Azure OpenAI)
    #   - cognitiveservices.azure.com  (AI Language, Document Intelligence, etc.)
    #   - search.windows.net       (Azure AI Search)
    # Use re.match() to check whether the endpoint matches.
    # Store your pattern in the variable below.
    pattern = ""  # TODO: replace with your regex pattern
    return {
        "service_name": service_name,
        "endpoint_valid": bool(re.match(pattern, endpoint)) if endpoint and pattern else False,
        "key_present": bool(key),
        "endpoint_pattern": pattern,
    }


def run_security_audit() -> dict:
    """Run a security audit on the project.

    Pre-implemented — students do not need to modify this function.
    See the Reference section in README.md for concepts.
    """
    configs = load_all_configs()
    all_keys = all(c.key for c in configs)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    activity_root = os.path.join(base_dir, "..")

    gitignore_path = os.path.join(activity_root, ".gitignore")
    gitignore_blocks = False
    if os.path.exists(gitignore_path):
        with open(gitignore_path) as f:
            gitignore_blocks = ".env" in f.read()

    no_hardcoded = True
    app_dir = os.path.join(activity_root, "app")
    if os.path.isdir(app_dir):
        for fname in os.listdir(app_dir):
            if fname.endswith(".py"):
                with open(os.path.join(app_dir, fname)) as f:
                    content = f.read()
                if "openai.azure.com" in content or "cognitiveservices.azure.com" in content:
                    if "your-" not in content and "example" not in content and "pattern" not in content:
                        no_hardcoded = False

    return {
        "total_services": len(REQUIRED_SERVICES),
        "all_keys_present": all_keys,
        "no_hardcoded_secrets": no_hardcoded,
        "gitignore_blocks_env": gitignore_blocks,
        "env_file_exists": os.path.exists(".env"),
        "auth_model_summary": compare_auth_models(),
    }


def compare_auth_models() -> str:
    """Compare authentication models for Azure AI services.

    Pre-implemented — students do not need to modify this function.
    See the Reference section in README.md for concepts.
    """
    return (
        "Key-based authentication is the simplest approach but keys can leak "
        "and there is no audit trail. RBAC uses Azure AD role assignments like "
        "Cognitive Services User for granular, auditable access but requires "
        "Azure AD setup. Managed Identity eliminates secrets from code entirely "
        "with auto-rotated credentials but only works in Azure-hosted environments."
    )


# ─── Assemble and Write Outputs ──────────────────────────────────────────────

def main():
    """Main activity function — build architecture, audit config, estimate costs."""

    # ── Part A: Architecture Design (writes design.json) ──
    print("PART A")

    # Load scenarios (used for requirement_summary in design.json)
    scenarios = load_scenarios()
    scenario_by_dept = {s["department"]: s for s in scenarios}

    # Display services for each scenario
    services = find_services(scenarios)
    if services:
        print(f"Valid services for each scenario:")
        for service in services:
            print(f"{service}: {services[service]}")

        # Build architecture decisions
        decisions = build_architecture_decisions()

        # Merge decisions with scenario summaries
        architecture = []
        for decision in decisions:
            dept = decision.get("department", "")
            scenario = scenario_by_dept.get(dept, {})
            architecture.append({
                "requirement_summary": scenario.get("pain_point", ""),
                **decision,
            })

        # Build shared resources
        shared = build_shared_resources()

        # Count unique services
        unique_services = set()
        for item in architecture:
            if item.get("primary_service"):
                unique_services.add(item["primary_service"])

        # Determine architecture status
        complete_entries = [a for a in architecture if a.get("primary_service")]
        if len(complete_entries) == len(scenarios) and shared.get("resource_group"):
            arch_status = "success"
        elif len(complete_entries) > 0:
            arch_status = "partial"
        else:
            arch_status = "error"

        # Write design.json
        design = {
            "task": "architect_platform",
            "status": arch_status,
            "outputs": {
                "architecture": {
                    "project_name": "Memphis City AI Platform",
                    "scenarios": architecture,
                    "shared_resources": shared,
                }
            },
            "metadata": {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "total_scenarios": len(scenarios),
                "unique_services_used": len(unique_services),
            },
        }
        write_design(design)
        print(f"Design written to design.json (status: {design['status']})")

    else:
        print("Finish find_services() before proceeding!")

    # ── Config Audit + Cost Estimates (writes result.json) ──
    print("\nPART B")

    # Validate service configs
    configs = load_all_configs()
    validations = []
    for config in configs:
        validation = validate_service_config(
            config.name, config.endpoint, config.key
        )
        validations.append(validation)

    # Run security audit
    audit = run_security_audit()

    # Estimate costs
    pricing = load_pricing()
    usage = load_usage()
    estimates = []
    for item in usage:
        estimate = estimate_cost(item, pricing)
        estimates.append(estimate)

    # Check budgets
    over_budget = check_budget(estimates)

    # Calculate total
    total_cost = sum(
        e.get("monthly_cost_usd", 0) for e in estimates
        if isinstance(e.get("monthly_cost_usd"), (int, float))
    )

    # Build monitoring plan (connected to over-budget departments)
    monitoring = build_monitoring_plan(estimates, over_budget)

    # Determine result status
    has_validations = any(v.get("service_name") for v in validations)
    has_audit = bool(audit.get("total_services"))
    has_estimates = any(e.get("department") for e in estimates)
    has_monitoring = bool(monitoring.get("metrics_to_track"))

    if has_validations and has_audit and has_estimates and has_monitoring:
        result_status = "success"
    elif has_validations or has_audit or has_estimates or has_monitoring:
        result_status = "partial"
    else:
        result_status = "error"

    # Write result.json
    result = {
        "task": "architect_platform",
        "status": result_status,
        "outputs": {
            "services_configured": validations,
            "security_audit": audit,
            "cost_estimates": estimates,
            "total_monthly_cost_usd": total_cost,
            "departments_over_budget": over_budget,
            "monitoring_plan": monitoring,
        },
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pricing_version": "2026-01",
            "currency": "USD",
            "environment": "development",
        },
    }

    write_result(result)
    print(f"Result written to result.json (status: {result['status']})")
    if over_budget:
        print(f"WARNING: {len(over_budget)} department(s) over budget: {over_budget}")
    print(f"Total estimated monthly cost: {format_currency(total_cost)}")


if __name__ == "__main__":
    main()
