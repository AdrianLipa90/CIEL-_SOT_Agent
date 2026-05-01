from __future__ import annotations

from typing import Any, Dict, List


def _pluck_text(item: Any) -> str:
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        for key in ("content", "text", "canonical_text", "canonical_action", "summary"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
        if "result" in item and isinstance(item["result"], dict):
            return _pluck_text(item["result"])
    return ""


def summarize_sector_retrieval(ciel_state: Dict[str, Any], *, max_items_per_channel: int = 2) -> Dict[str, List[str]]:
    sector_memory = ciel_state.get("sector_memory") if isinstance(ciel_state.get("sector_memory"), dict) else {}
    retrieval = {}
    governed = sector_memory.get("governed_retrieval") if isinstance(sector_memory.get("governed_retrieval"), dict) else {}
    summary: Dict[str, List[str]] = {}

    ranked = governed.get("ranked") if isinstance(governed.get("ranked"), list) else []
    ranked_lines: List[str] = []
    for row in ranked[: max(1, max_items_per_channel * 2)]:
        if not isinstance(row, dict):
            continue
        txt = _pluck_text(row)
        if not txt:
            txt = str(row.get("text", "") or "").strip()
        if not txt:
            continue
        channel = str(row.get("channel", "memory"))
        hq = row.get("holonomy_quality")
        pa = row.get("phase_alignment")
        tags: List[str] = [channel]
        if isinstance(hq, (int, float)):
            tags.append(f"hq={float(hq):.2f}")
        if isinstance(pa, (int, float)):
            tags.append(f"pa={float(pa):.2f}")
        ranked_lines.append(f"[{', '.join(tags)}] {txt[:200]}")
    if ranked_lines:
        summary["ranked"] = ranked_lines

    if isinstance(governed.get("by_channel"), dict):
        retrieval = governed.get("by_channel")
    elif isinstance(sector_memory.get("retrieval"), dict):
        retrieval = sector_memory.get("retrieval")
    for channel, items in retrieval.items():
        texts: List[str] = []
        if isinstance(items, list):
            for item in items[:max_items_per_channel]:
                txt = _pluck_text(item)
                if txt:
                    texts.append(txt[:200])
        elif isinstance(items, dict):
            txt = _pluck_text(items)
            if txt:
                texts.append(txt[:200])
        if texts:
            summary[str(channel)] = texts
    return summary



def _is_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _semantic_state_snippets(ciel_state: Dict[str, Any], *, max_items_per_channel: int = 2) -> List[str]:
    snippets: List[str] = []
    retrieval_summary = summarize_sector_retrieval(ciel_state, max_items_per_channel=max_items_per_channel)
    ranked = retrieval_summary.get("ranked", [])
    if ranked:
        snippets.append("Retrieved semantic memory:")
        for line in ranked[:max_items_per_channel * 2]:
            snippets.append(f"- {line}")

    for channel, items in retrieval_summary.items():
        if channel == "ranked":
            continue
        if not items:
            continue
        snippets.append(f"{channel.capitalize()} channel:")
        for item in items[:max_items_per_channel]:
            snippets.append(f"- {item}")

    sem_labels = ciel_state.get("semantic_labels")
    if isinstance(sem_labels, list) and sem_labels:
        labels = [str(x).strip() for x in sem_labels if str(x).strip()]
        if labels:
            snippets.append("Semantic labels: " + ", ".join(labels[:8]))

    memory_score = ciel_state.get("memory_score")
    if isinstance(memory_score, (int, float)):
        snippets.append(f"Memory score: {float(memory_score):.3f}")

    nonlocal_rt = ciel_state.get("nonlocal_runtime") if isinstance(ciel_state.get("nonlocal_runtime"), dict) else {}
    if nonlocal_rt:
        semantic_key = nonlocal_rt.get("semantic_key")
        coherent_fraction = nonlocal_rt.get("coherent_fraction")
        if _is_nonempty_text(semantic_key):
            snippets.append(f"Nonlocal semantic key: {semantic_key}")
        if isinstance(coherent_fraction, (int, float)):
            snippets.append(f"Nonlocal coherent fraction: {float(coherent_fraction):.3f}")

    euler_bridge = ciel_state.get("euler_bridge") if isinstance(ciel_state.get("euler_bridge"), dict) else {}
    if euler_bridge:
        mem_key = euler_bridge.get("memory_semantic_key")
        if _is_nonempty_text(mem_key):
            snippets.append(f"Euler bridge memory key: {mem_key}")

    runtime_policy = ciel_state.get("runtime_policy") if isinstance(ciel_state.get("runtime_policy"), dict) else {}
    if runtime_policy:
        mode = runtime_policy.get("response_strategy") or runtime_policy.get("control_mode")
        if _is_nonempty_text(mode):
            snippets.append(f"Runtime policy: {mode}")
        durable = runtime_policy.get("durable_write_allowed")
        if isinstance(durable, bool):
            snippets.append(f"Durable write allowed: {str(durable).lower()}")

    return snippets


def build_semantic_speech_context(ciel_state: Dict[str, Any], *, max_items_per_channel: int = 2, max_chars: int = 1600) -> Dict[str, Any]:
    """Build a compact speech-ready semantic brief from M3 and nearby state."""
    snippets = _semantic_state_snippets(ciel_state, max_items_per_channel=max_items_per_channel)
    text = "\n".join(snippets)
    if len(text) > max_chars:
        text = text[: max_chars - 20].rstrip() + "\n[...truncated...]"
    return {
        "text": text,
        "snippets": snippets,
        "retrieval": summarize_sector_retrieval(ciel_state, max_items_per_channel=max_items_per_channel),
    }
