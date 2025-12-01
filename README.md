# healthflow-agent
# Health Insights Agent — ADK-Powered Healthcare Assistant

> Sample GitHub-style repository for the Kaggle **5-Day AI Agents Intensive Capstone**.

**Track:** Agents for Good (Healthcare)  
**Tools:** Google Agent Development Kit (ADK), Gemini (via ADK), Vertex AI Agent Engine (optional deployment)

---

## Problem Statement

Patients and clinicians are overwhelmed by unstructured medical information:
- Lab reports and discharge summaries are hard for non-experts to understand.
- Chronic disease metrics (e.g., diabetes, hypertension) are not tracked in a structured, explainable way.
- Patient scheduling and follow‑ups are often manual and error‑prone.

This leads to missed follow‑ups, poor adherence to care plans, and low health literacy.

---

## Solution Overview

**Health Insights Agent** is a **multi‑agent system** built with **Google ADK** that:

1. **Analyzes medical reports** (e.g., labs, imaging summaries, discharge notes) and produces simplified explanations.
2. **Tracks disease progression** using patient time‑series metrics and generates monitoring insights.
3. **Proposes follow‑up schedules** and reminders based on guidelines (non‑diagnostic, explanation‑only).
4. Uses **sessions & memory** to remember patient history across interactions.
5. Is instrumented with **logs, traces, and metrics** for debugging and evaluation.
6. Can be deployed to **Vertex AI Agent Engine** using `AdkApp`.

The project is intentionally scoped as a **course-style capstone**: safe, explainable, non‑diagnostic, and easy to extend.

---

## Architecture

The system is built around a root orchestrator agent and three specialized sub‑agents:

- `report_insights_agent` — parses and summarizes medical reports into patient‑friendly language and clinician, structured bullet points.
- `disease_monitor_agent` — takes time‑stamped metrics (e.g. HbA1c, BP logs) and produces trend analysis & alerts.
- `scheduling_agent` — suggests follow‑up schedules, simple reminders, and questions to ask the doctor.

```text
[User / Clinician]
         |
         v
[health_insights_orchestrator (LlmAgent)]
    |             |                 |
    v             v                 v
[report_insights] [disease_monitor] [scheduling]
    |                  |               |
    +-----------> Shared tools <-------+
                   (parsers, memory)
         |
         v
     Structured JSON + explanations
```

ADK features used:

- **Multi-agent:** orchestrator with three sub‑agents.
- **Tools:** custom Python tools for parsing reports and managing in‑memory “patient records”.
- **Sessions & Memory:** `InMemorySessionService` via `AdkApp`, plus a simple in‑code patient store.
- **Observability:** simple logging helper for traces & metrics.
- **A2A‑ready design:** the root agent can be wrapped in an `AdkApp` and exposed via HTTP for A2A communication.
- **Evaluation hooks:** a basic test in `tests/test_agent.py` that exercises the pipeline.

---

## Repository Structure

```text
health_insights_agent/
├── health_insights_agent/
│   ├── __init__.py
│   ├── agent.py                # root orchestrator, AdkApp wiring
│   ├── config.py               # model, environment config
│   ├── tools.py                # shared tools (parsers, patient store)
│   └── sub_agents/
│       ├── report_insights.py  # medical report analysis agent
│       ├── disease_monitor.py  # disease monitoring agent
│       └── scheduling.py       # scheduling & follow-up agent
├── deployment/
│   └── Dockerfile              # example container spec
├── tests/
│   └── test_agent.py           # minimal integration test
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Installation

1. **Create a virtual environment** (Python 3.10+ recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Gemini / Vertex AI credentials**

   - Make sure you have a **Google AI Studio** or **Vertex AI** project.
   - Set the environment variables expected by ADK (see ADK docs). For local development, this usually means:
     - `GOOGLE_APPLICATION_CREDENTIALS` for service account key, **or**
     - proper `gcloud auth application-default login` set up.

   No API keys are hard‑coded anywhere in this repo.

---

## Running the Agent (Local ADK Web UI)

ADK provides a handy web UI for debugging:

```bash
# From the repo root
adk web
```

Then open the printed local URL in your browser and select the `health_insights_orchestrator` agent.

You can also run the `AdkApp` FastAPI server directly:

```bash
python -m health_insights_agent.agent
```

This starts a FastAPI app (via `AdkApp`) on `http://0.0.0.0:8080` by default.

---

## How This Maps to the Kaggle Capstone Rubric

- **Track:** Agents for Good (healthcare accessibility).
- **Multi-agent system:** orchestrator + 3 sub‑agents.
- **Tools:** custom parsing and memory tools defined as ADK tools.
- **Sessions & memory:** handled by `AdkApp` + simple in‑code store.
- **Observability:** lightweight logging for each agent step.
- **Agent evaluation:** test file + clear prompts so you can extend with eval sets.
- **Deployment:** `deployment/Dockerfile` can be adapted to Cloud Run / Agent Engine.

You can copy‑paste parts of this README into your **Kaggle Capstone writeup** and extend with your own experiments and screenshots.

---

## Safety Notice

This project is for **educational & demonstration purposes only**.  
It **does not** provide medical diagnoses and must not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any medical decision.
