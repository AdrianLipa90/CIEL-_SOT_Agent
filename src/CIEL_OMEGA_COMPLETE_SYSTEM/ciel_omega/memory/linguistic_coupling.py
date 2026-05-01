"""Lightweight linguistic-semantic coupling utilities for CIEL/Ω.

This module adds a conservative, dependency-free scoring layer that measures
how much grammatical shape supports semantic anchoring. It is intentionally
heuristic: no POS tagger, no parser, just a stable vector of surface signals.

The goal is not to "understand" language magically. The goal is to give the
memory system a measurable bridge between form and meaning so fragments,
run-on text, and semantically anchored statements are not all treated alike.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import re
from typing import Iterable

import numpy as np

_WORD_RE = re.compile(r"[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+(?:'[\w]+)?", re.UNICODE)
_SENTENCE_END_RE = re.compile(r"[.!?]+$")
_CLAUSE_SPLIT_RE = re.compile(r"[,:;\-–—]+")

# Small bilingual function-word inventory. This is not a grammar parser.
_FUNCTION_WORDS = {
    # English
    "a", "an", "the", "and", "or", "but", "if", "then", "when", "while",
    "of", "to", "for", "from", "in", "on", "at", "by", "with", "without",
    "as", "is", "are", "was", "were", "be", "been", "being", "do", "does",
    "did", "have", "has", "had", "will", "would", "can", "could", "should",
    "may", "might", "must", "that", "this", "these", "those", "it", "its",
    "we", "you", "he", "she", "they", "them", "our", "your", "their",
    # Polish
    "i", "a", "ale", "lub", "oraz", "jeśli", "gdy", "kiedy", "w", "na",
    "do", "od", "z", "ze", "po", "przez", "dla", "bez", "jak", "jest",
    "są", "był", "była", "było", "byli", "były", "będzie", "może", "musi",
    "to", "ta", "ten", "te", "tego", "tej", "tych", "mu", "jej", "ich",
    "nas", "was", "się", "nie", "co", "kto", "który", "która", "które",
}

# A tiny verb-ish inventory. Enough to detect "sentence-ness" in a lightweight way.
_VERB_HINTS = {
    "is", "are", "was", "were", "be", "been", "being", "do", "does", "did",
    "have", "has", "had", "want", "know", "think", "say", "see", "make",
    "go", "take", "give", "work", "use", "prefer", "support", "align",
    "preferuje", "lubi", "chce", "wie", "myśli", "mówi", "widzi", "robi",
    "idzie", "bierze", "daje", "pracuje", "używa", "wspiera", "wyrównuje",
}

_NEGATION_WORDS = {"not", "no", "never", "none", "n't", "nie", "nigdy", "żaden", "żadna", "żadne"}


@dataclass(frozen=True)
class LinguisticCouplingProfile:
    """Surface-level coupling between language form and meaning."""

    token_count: int
    content_count: int
    clause_count: int
    has_terminal_punctuation: bool
    lexical_diversity: float
    content_balance: float
    verb_signal: float
    semantic_anchor: float
    negation_consistency: float
    grammaticality: float
    coupling: float

    def as_vector(self) -> np.ndarray:
        return np.array(
            [
                self.lexical_diversity,
                self.content_balance,
                self.verb_signal,
                self.semantic_anchor,
                self.negation_consistency,
                self.grammaticality,
            ],
            dtype=float,
        )


@dataclass(frozen=True)
class LinguisticSemanticCoupling:
    """Bundle of language-form and meaning-side scores."""

    profile: LinguisticCouplingProfile
    content_overlap: float
    shape_coherence: float

    @property
    def coupling(self) -> float:
        return self.profile.coupling

    @property
    def grammaticality(self) -> float:
        return self.profile.grammaticality

    @property
    def semantic_anchor(self) -> float:
        return self.profile.semantic_anchor


def _tokenize(text: str) -> list[str]:
    return [m.group(0).lower() for m in _WORD_RE.finditer(text)]


def _stem(token: str, stem_len: int = 5) -> str:
    token = token.lower()
    return token[:stem_len] if len(token) > stem_len else token


def _semantic_key_stems(semantic_key: str) -> set[str]:
    tokens = [t for t in _tokenize(semantic_key) if t not in _FUNCTION_WORDS and t not in _NEGATION_WORDS]
    return {_stem(t) for t in tokens}


def _content_tokens(tokens: Iterable[str]) -> list[str]:
    return [t for t in tokens if t not in _FUNCTION_WORDS and t not in _NEGATION_WORDS and len(t) > 2]


def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def analyze_linguistic_coupling(text: str, semantic_key: str, is_negated: bool = False) -> LinguisticSemanticCoupling:
    """Return a conservative coupling profile for a text/meaning pair.

    The heuristic is intentionally transparent:
    - grammaticality comes from sentence closure, clause shape, token balance,
      and the presence of at least one verb-like signal;
    - semantic anchoring comes from overlap between the text and the semantic key;
    - negation consistency rewards explicit negation when the text is negated.
    """
    raw = str(text).strip()
    tokens = _tokenize(raw)
    token_count = len(tokens)
    content = _content_tokens(tokens)
    content_count = len(content)
    unique_content = len(set(content))
    clause_count = max(1, len(_CLAUSE_SPLIT_RE.split(raw)) + raw.count(";") + raw.count(","))

    if token_count == 0:
        profile = LinguisticCouplingProfile(
            token_count=0,
            content_count=0,
            clause_count=0,
            has_terminal_punctuation=False,
            lexical_diversity=0.0,
            content_balance=0.0,
            verb_signal=0.0,
            semantic_anchor=0.0,
            negation_consistency=0.0,
            grammaticality=0.0,
            coupling=0.0,
        )
        return LinguisticSemanticCoupling(profile=profile, content_overlap=0.0, shape_coherence=0.0)

    has_terminal_punctuation = bool(_SENTENCE_END_RE.search(raw))
    lexical_diversity = unique_content / max(1, content_count)
    content_ratio = content_count / max(1, token_count)

    # Prefer a moderately dense signal: not too fragmentary, not too bloated.
    content_balance = 1.0 - min(1.0, abs(content_ratio - 0.58) / 0.58)

    # Verb-ish signal: direct hint if a known verb appears, else suffix-based fallback.
    verb_hits = sum(1 for t in tokens if t in _VERB_HINTS or t.endswith(("ed", "ing", "en", "ło", "ły", "cie", "esz", "ał", "ił", "ył")))
    verb_signal = min(1.0, verb_hits / max(1, min(3, token_count)))

    key_stems = _semantic_key_stems(semantic_key)
    content_stems = {_stem(t) for t in content}
    overlap = len(key_stems & content_stems)
    content_overlap = overlap / max(1, len(key_stems))
    semantic_anchor = 0.65 * content_overlap + 0.35 * min(1.0, overlap / max(1, len(content_stems)))

    negation_tokens = [t for t in tokens if t in _NEGATION_WORDS]
    negation_consistency = 1.0 if (bool(negation_tokens) == bool(is_negated)) else 0.62

    punctuation_bonus = 1.0 if has_terminal_punctuation else 0.82
    clause_penalty = 1.0 / (1.0 + abs(clause_count - 1.0) * 0.18)
    length_bonus = _sigmoid((token_count - 5.0) / 2.2) * _sigmoid((24.0 - token_count) / 3.0)

    base_grammar = np.array([
        punctuation_bonus,
        clause_penalty,
        length_bonus,
        0.55 + 0.45 * content_balance,
        0.60 + 0.40 * verb_signal,
        0.70 + 0.30 * lexical_diversity,
    ], dtype=float)
    weights = np.array([0.16, 0.15, 0.18, 0.18, 0.18, 0.15], dtype=float)
    grammaticality = float(np.clip(base_grammar @ weights, 0.0, 1.0))

    coupling = float(np.clip(
        0.42 * grammaticality
        + 0.34 * semantic_anchor
        + 0.12 * content_balance
        + 0.12 * negation_consistency,
        0.0,
        1.0,
    ))

    profile = LinguisticCouplingProfile(
        token_count=token_count,
        content_count=content_count,
        clause_count=clause_count,
        has_terminal_punctuation=has_terminal_punctuation,
        lexical_diversity=float(np.clip(lexical_diversity, 0.0, 1.0)),
        content_balance=float(np.clip(content_balance, 0.0, 1.0)),
        verb_signal=float(np.clip(verb_signal, 0.0, 1.0)),
        semantic_anchor=float(np.clip(semantic_anchor, 0.0, 1.0)),
        negation_consistency=float(np.clip(negation_consistency, 0.0, 1.0)),
        grammaticality=grammaticality,
        coupling=coupling,
    )
    return LinguisticSemanticCoupling(
        profile=profile,
        content_overlap=float(np.clip(content_overlap, 0.0, 1.0)),
        shape_coherence=float(np.clip(0.55 * grammaticality + 0.45 * semantic_anchor, 0.0, 1.0)),
    )


def lexical_semantic_matrix(text: str, semantic_key: str) -> np.ndarray:
    """Return a compact feature matrix for diagnostics and future vectorisation."""
    coupling = analyze_linguistic_coupling(text, semantic_key)
    return np.stack([coupling.profile.as_vector()], axis=0)
