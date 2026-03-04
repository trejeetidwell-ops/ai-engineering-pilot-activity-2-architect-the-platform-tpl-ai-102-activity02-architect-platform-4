"""
Utility functions for Activity 2 - Architect the Platform.

These helpers are provided for you -- no changes needed here.
"""

import json
import os


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
DESIGN_PATH = os.path.join(PROJECT_ROOT, "design.json")
RESULT_PATH = os.path.join(PROJECT_ROOT, "result.json")


def write_design(design: dict, path: str = DESIGN_PATH) -> None:
    """Write the architecture design to design.json.

    Args:
        design: Dictionary with the architecture design.
        path: File path to write (defaults to project root design.json).
    """
    with open(path, "w") as f:
        json.dump(design, f, indent=2)


def read_design(path: str = DESIGN_PATH) -> dict:
    """Read and return the design.json file.

    Args:
        path: File path to read.

    Returns:
        Parsed JSON as a dictionary.

    Raises:
        FileNotFoundError: If design.json does not exist.
    """
    with open(path) as f:
        return json.load(f)


def write_result(result: dict, path: str = RESULT_PATH) -> None:
    """Write audit and cost results to result.json.

    Args:
        result: Dictionary with task, status, outputs, metadata fields.
        path: File path to write (defaults to project root result.json).
    """
    with open(path, "w") as f:
        json.dump(result, f, indent=2)


def read_result(path: str = RESULT_PATH) -> dict:
    """Read and return the result.json file.

    Args:
        path: File path to read.

    Returns:
        Parsed JSON as a dictionary.

    Raises:
        FileNotFoundError: If result.json does not exist.
    """
    with open(path) as f:
        return json.load(f)
