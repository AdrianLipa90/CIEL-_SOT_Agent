"""CIEL/Ω Quantum Consciousness Suite — Engine package.

Copyright (c) 2025 Adrian Lipa / Intention Lab
Licensed under the CIEL Research Non-Commercial License v1.1.
"""

from __future__ import annotations

from typing import Any

__all__: list[str] = ["CielEngine", "LLMBackendBundle", "build_default_bundle"]


def __getattr__(name: str) -> Any:
    if name == "CielEngine":
        from .engine import CielEngine as _CielEngine

        return _CielEngine
    if name in {"LLMBackendBundle", "build_default_bundle"}:
        from .llm_registry import LLMBackendBundle as _LLMBackendBundle, build_default_bundle as _build_default_bundle

        return _LLMBackendBundle if name == "LLMBackendBundle" else _build_default_bundle
    raise AttributeError(name)
