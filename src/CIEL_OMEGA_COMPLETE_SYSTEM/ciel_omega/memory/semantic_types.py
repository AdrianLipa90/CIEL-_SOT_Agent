"""CIEL/Ω Memory Architecture - Semantic Memory Types

Data structures for M3 SemanticMemory channel.
Conservative semantic consolidation from episodic traces.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class SemanticTrace:
    timestamp: float
    source_episode_ids: List[str]
    semantic_key: str
    content: str
    phase: float
    phase_diff: float
    identity_alignment: float
    confidence: float
    contradiction_score: float
    novelty_score: float
    is_negated: bool = False
    eba_defect: float = 0.5   # EBA defect magnitude at observation time
    berry_phase: float = 0.0  # geometric phase (phase_diff, as angle on Bloch sphere)
    grammar_score: float = 0.0
    semantic_anchor_score: float = 0.0
    linguistic_coupling: float = 0.0


@dataclass
class SemanticCandidate:
    semantic_key: str
    canonical_text: str
    aliases: List[str] = field(default_factory=list)
    trace_support_count: int = 0
    candidate_confirmation_count: int = 0
    mean_identity_alignment: float = 0.0
    mean_confidence: float = 0.0
    stability: float = 0.0
    contradiction_score: float = 0.0
    mean_grammar_score: float = 0.0
    mean_semantic_anchor: float = 0.0
    mean_linguistic_coupling: float = 0.0
    status: str = "detected"  # detected, mature, blocked
    consolidated: bool = False
    is_negated: bool = False

    def is_detected(self, min_trace_support: int) -> bool:
        return self.trace_support_count >= min_trace_support and self.status != "blocked"

    def is_mature(self, min_confirmations: int, min_alignment: float,
                  min_stability: float, max_contradiction: float) -> bool:
        return (
            self.candidate_confirmation_count >= min_confirmations and
            self.mean_identity_alignment >= min_alignment and
            self.stability >= min_stability and
            self.contradiction_score <= max_contradiction and
            self.status != "blocked"
        )


@dataclass
class SemanticItem:
    semantic_key: str
    canonical_text: str
    aliases: List[str]
    phase: float
    confidence: float
    stability: float
    identity_alignment: float
    provenance_episode_ids: List[str]
    created_at: float
    updated_at: float
    version: int = 1
    status: str = "active"  # active, contested, deprecated
    is_negated: bool = False
    berry_phase: float = 0.0  # mean geometric phase across consolidating traces
    grammar_score: float = 0.0
    semantic_anchor_score: float = 0.0
    linguistic_coupling: float = 0.0


@dataclass
class SemanticConsolidationScore:
    stability: float
    identity_alignment: float
    confidence: float
    repeated_support: float
    contradiction: float
    eba_contribution: float = 0.0  # geometric: high when EBA defect is low (topological order)
    linguistic_coherence: float = 0.0
    w_s: float = 0.22
    w_a: float = 0.20
    w_c: float = 0.15
    w_r: float = 0.18
    w_e: float = 0.12  # EBA geometric weight
    w_l: float = 0.13  # linguistic-semantic coupling weight
    w_x: float = 0.28

    def compute_total(self) -> float:
        return (
            self.w_s * self.stability +
            self.w_a * self.identity_alignment +
            self.w_c * self.confidence +
            self.w_r * self.repeated_support +
            self.w_e * self.eba_contribution +
            self.w_l * self.linguistic_coherence -
            self.w_x * self.contradiction
        )


__all__ = [
    'SemanticTrace',
    'SemanticCandidate',
    'SemanticItem',
    'SemanticConsolidationScore',
]
