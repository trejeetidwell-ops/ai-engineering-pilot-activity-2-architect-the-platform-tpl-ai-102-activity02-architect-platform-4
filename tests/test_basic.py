"""Visible tests for Activity 2 - Architect the Platform.

Students can run these tests to check their work before submitting.
Run with: pytest tests/ -v
"""

import json
import os
import re

import pytest


LAB_ROOT = os.path.join(os.path.dirname(__file__), "..")
DESIGN_PATH = os.path.join(LAB_ROOT, "design.json")
RESULT_PATH = os.path.join(LAB_ROOT, "result.json")
MAIN_PATH = os.path.join(LAB_ROOT, "app", "main.py")


@pytest.fixture
def design():
    """Load the student's design.json."""
    if not os.path.exists(DESIGN_PATH):
        pytest.skip("design.json not found - run 'python app/main.py' first")
    with open(DESIGN_PATH) as f:
        return json.load(f)


@pytest.fixture
def result():
    """Load the student's result.json."""
    if not os.path.exists(RESULT_PATH):
        pytest.skip("result.json not found - run 'python app/main.py' first")
    with open(RESULT_PATH) as f:
        return json.load(f)


# ═══ Canary test ═══════════════════════════════════════════════════════════

def test_result_exists():
    """result.json file must exist."""
    assert os.path.exists(RESULT_PATH), (
        "result.json not found. Run 'python app/main.py' to generate it."
    )


def test_design_exists():
    """design.json file must exist."""
    assert os.path.exists(DESIGN_PATH), (
        "design.json not found. Run 'python app/main.py' to generate it."
    )


# ═══ design.json contract tests ═══════════════════════════════════════════

def test_design_required_fields(design):
    """design.json must have required top-level fields."""
    for field in ("task", "status", "outputs", "metadata"):
        assert field in design, f"Missing required field in design.json: {field}"


def test_design_task_name(design):
    """Task must be 'architect_platform'."""
    assert design["task"] == "architect_platform", (
        f"Expected task 'architect_platform', got '{design['task']}'"
    )


def test_design_status_valid(design):
    """Status must be one of the valid values."""
    assert design["status"] in ("success", "partial", "error"), (
        f"Invalid status: {design['status']}. Must be success, partial, or error."
    )


# ═══ Architecture validation ══════════════════════════════════════════════

def test_scenarios_present(design):
    """outputs.architecture.scenarios must be a list with 6 items."""
    arch = design.get("outputs", {}).get("architecture", {})
    scenarios = arch.get("scenarios", [])
    assert isinstance(scenarios, list), "scenarios must be a list"
    assert len(scenarios) == 6, (
        f"Expected 6 scenarios, got {len(scenarios)}. "
        "Make sure you process all city department scenarios."
    )


def test_scenario_required_keys(design):
    """Each scenario must have department, primary_service, justification, responsible_ai_considerations."""
    arch = design.get("outputs", {}).get("architecture", {})
    scenarios = arch.get("scenarios", [])
    if not scenarios:
        pytest.skip("No scenarios found - implement find_services() and build_architecture_decisions() first")

    required_keys = [
        "department",
        "primary_service",
        "sdk_package",
        "justification",
        "responsible_ai_considerations",
    ]
    for i, scenario in enumerate(scenarios):
        for key in required_keys:
            assert key in scenario, (
                f"Scenario {i} ({scenario.get('department', 'unknown')}) "
                f"is missing required key: {key}"
            )


def test_shared_resources_present(design):
    """outputs.architecture.shared_resources must exist and not be empty."""
    arch = design.get("outputs", {}).get("architecture", {})
    shared = arch.get("shared_resources", {})
    assert isinstance(shared, dict), "shared_resources must be a dict"
    assert len(shared) > 0, (
        "shared_resources is empty. Implement build_shared_resources()."
    )


# ═══ result.json contract tests ═══════════════════════════════════════════

def test_result_required_fields(result):
    """result.json must have required top-level fields."""
    for field in ("task", "status", "outputs", "metadata"):
        assert field in result, f"Missing required field in result.json: {field}"


def test_result_task_name(result):
    """Task must be 'architect_platform'."""
    assert result["task"] == "architect_platform", (
        f"Expected task 'architect_platform', got '{result['task']}'"
    )


# ═══ Cost estimation validation ═══════════════════════════════════════════

def test_cost_estimates_present(result):
    """outputs.cost_estimates must be a list with at least 6 items."""
    estimates = result.get("outputs", {}).get("cost_estimates", [])
    assert isinstance(estimates, list), "cost_estimates must be a list"
    assert len(estimates) >= 6, (
        f"Expected at least 6 cost estimates, got {len(estimates)}"
    )


def test_costs_are_numeric(result):
    """Each estimate's monthly_cost_usd must be a number >= 0."""
    estimates = result.get("outputs", {}).get("cost_estimates", [])
    for i, est in enumerate(estimates):
        cost = est.get("monthly_cost_usd")
        assert isinstance(cost, (int, float)), (
            f"Estimate {i}: monthly_cost_usd must be a number, got {type(cost).__name__}"
        )
        assert cost >= 0, (
            f"Estimate {i}: monthly_cost_usd must be >= 0, got {cost}"
        )


def test_total_cost_present(result):
    """outputs.total_monthly_cost_usd must be a number >= 0."""
    total = result.get("outputs", {}).get("total_monthly_cost_usd")
    assert isinstance(total, (int, float)), (
        f"total_monthly_cost_usd must be a number, got {type(total).__name__}"
    )
    assert total >= 0, (
        f"total_monthly_cost_usd must be >= 0, got {total}"
    )


# ═══ Monitoring plan validation ═══════════════════════════════════════════

def test_monitoring_plan_present(result):
    """outputs.monitoring_plan must have metrics_to_track (>= 3) and alert_rules (>= 2)."""
    plan = result.get("outputs", {}).get("monitoring_plan", {})
    metrics = plan.get("metrics_to_track", [])
    alerts = plan.get("alert_rules", [])
    assert isinstance(metrics, list), "metrics_to_track must be a list"
    assert len(metrics) >= 3, (
        f"Expected at least 3 metrics to track, got {len(metrics)}"
    )
    assert isinstance(alerts, list), "alert_rules must be a list"
    assert len(alerts) >= 2, (
        f"Expected at least 2 alert rules (one per over-budget department), got {len(alerts)}"
    )
    for i, rule in enumerate(alerts):
        assert "department" in rule, (
            f"Alert rule {i} missing 'department' key. "
            "Each alert must target a specific over-budget department."
        )
        assert "condition" in rule, f"Alert rule {i} missing 'condition' key"
        assert "action" in rule, f"Alert rule {i} missing 'action' key"


# ═══ Secrets hygiene ══════════════════════════════════════════════════════

def test_no_hardcoded_secrets():
    """main.py must not contain hardcoded API keys or secrets."""
    with open(MAIN_PATH) as f:
        source = f.read()

    suspicious_patterns = [
        r'["\']https?://\S+\.cognitiveservices\.azure\.com\S*["\']',
        r'["\'][A-Fa-f0-9]{32}["\']',
        r'api_key\s*=\s*["\'][^"\']+["\']',
        r'endpoint\s*=\s*["\']https?://[^"\']+["\']',
    ]

    for pattern in suspicious_patterns:
        matches = re.findall(pattern, source)
        real_matches = [
            m for m in matches
            if "example" not in m.lower()
            and "your-" not in m.lower()
            and "placeholder" not in m.lower()
            and "TODO" not in m
        ]
        assert len(real_matches) == 0, (
            f"Possible hardcoded credential found in main.py: {real_matches[0][:50]}... "
            "Use .env file and os.getenv() instead."
        )


def test_gitignore_has_env():
    """The .gitignore file must include .env to prevent committing secrets."""
    gitignore_path = os.path.join(LAB_ROOT, ".gitignore")
    if not os.path.exists(gitignore_path):
        pytest.fail(".gitignore file not found - create one with '.env' in it")

    with open(gitignore_path) as f:
        content = f.read()

    assert ".env" in content, (
        ".gitignore must include '.env' to prevent committing secrets"
    )


def test_env_example_exists():
    """.env.example must exist and contain only placeholder values."""
    env_example_path = os.path.join(LAB_ROOT, ".env.example")
    assert os.path.exists(env_example_path), (
        ".env.example not found. It should document required environment variables."
    )

    with open(env_example_path) as f:
        content = f.read()

    real_url_pattern = r'https://[a-z0-9-]+\.(openai\.azure\.com|cognitiveservices\.azure\.com|search\.windows\.net)'
    matches = re.findall(real_url_pattern, content)
    # Filter out placeholder URLs that contain "your-"
    real_matches = [
        m for m in re.finditer(real_url_pattern, content)
        if "your-" not in m.group(0)
    ]
    assert len(real_matches) == 0, (
        ".env.example should contain only placeholder values like "
        "'https://your-resource.openai.azure.com/', not real endpoints."
    )
