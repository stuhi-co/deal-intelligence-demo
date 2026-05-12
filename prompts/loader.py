"""Prompt version loader utilities.

Provides shared functions for dynamically loading prompt versions.
Used by individual prompt __init__.py files to avoid code duplication.
"""

import importlib
from types import ModuleType


def load_version(package: str, version: str) -> ModuleType:
    """Dynamically load a prompt version module.

    Args:
        package: The package name (use __name__ from the calling module)
        version: Version string (e.g., "v1.0", "v1.1")

    Returns:
        The loaded module

    Raises:
        ModuleNotFoundError: If version file doesn't exist

    Example:
        # In prompts/concept_inferrer/__init__.py
        from src.core.prompts.loader import load_version

        PROMPT_VERSION = "v1.0"
        _current = load_version(__name__, PROMPT_VERSION)
    """
    module_name = version.replace(".", "_")  # v1.0 -> v1_0
    return importlib.import_module(f".{module_name}", package=package)


def list_versions(package: str) -> list[str]:
    """List all available versions for a prompt package.

    Args:
        package: The package name (use __name__ from the calling module)

    Returns:
        List of version strings (e.g., ["v1.0", "v1.1", "v2.0"])

    Example:
        from src.core.prompts.loader import list_versions
        versions = list_versions(__name__)  # ["v1.0", "v1.1"]
    """
    import pkgutil
    import re

    # Get the actual module to find its path
    pkg_module = importlib.import_module(package)

    versions = []
    version_pattern = re.compile(r"^v(\d+)_(\d+)$")

    for importer, modname, ispkg in pkgutil.iter_modules(pkg_module.__path__):
        match = version_pattern.match(modname)
        if match:
            major, minor = match.groups()
            versions.append(f"v{major}.{minor}")

    return sorted(versions)
