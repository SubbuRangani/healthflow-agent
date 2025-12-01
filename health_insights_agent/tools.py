"""Shared tools for the Health Insights Agent.

NOTE: These are simple Python functions exposed as ADK tools.
They do **not** call any non-Google AI providers.
"""

from typing import Dict, Any, List
import datetime as _dt


_PATIENT_STORE: Dict[str, Dict[str, Any]] = {}


def upsert_patient_record(patient_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Create or update an in-memory patient record.

    This is intentionally simple for the capstone. In real-world use,
    you'd plug this into a proper database behind an authenticated API.
    """
    record = _PATIENT_STORE.get(patient_id, {})
    record.update(data)
    record.setdefault("updated_at", _dt.datetime.utcnow().isoformat())
    _PATIENT_STORE[patient_id] = record
    return record


def get_patient_record(patient_id: str) -> Dict[str, Any]:
    """Fetch a patient record from the in-memory store.

    If it doesn't exist, returns an empty record so the agent
    can decide what to do next.
    """
    return _PATIENT_STORE.get(patient_id, {})


def parse_lab_report(raw_text: str) -> Dict[str, Any]:
    """Very lightweight lab report parser.

    The goal here is not perfect parsing, but giving the agent a
    structured starting point. The LLM will refine this further.
    """
    # Simple heuristic demo: look for lines that look like "NAME: value unit"
    labs: List[Dict[str, str]] = []
    for line in raw_text.splitlines():
        if ":" in line:
            name, rest = line.split(":", 1)
            labs.append({"name": name.strip(), "raw_value": rest.strip()})
    return {"labs": labs}
