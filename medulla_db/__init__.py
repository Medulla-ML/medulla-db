# type: ignore[attr-defined]
"""Vector Database plugin for Medulla"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


def run():
    print("framework.typeA.plugin1 starting")
    print("framework.typeA.plugin1 finishing")


version: str = get_version()
