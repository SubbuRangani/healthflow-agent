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
- Patient scheduling and follow-ups are often manual and error-prone.

This leads to missed follow-ups, poor adherence to care plans, and low health literacy.

---

## Solution Overview

**Health Insights Agent** is a **multi-agent system** built with **Google ADK** that:

1. **Analyzes medical reports** (e.g., labs, imaging summaries, discharge notes) and produces simplified explanations.
2. **Tracks disease progression** using patient time-series metrics and generates monitoring insights.
3. **Proposes follow-up schedules** and reminders based on guidelines (non-diagnostic, explanation-only).
4. Uses **sessions & memory** to remember patient history across interactions.
5. Is instrumented with **logs, traces, and metrics** for debugging and evaluation.
6. Can be deployed to **Vertex AI Agent Engine** using `AdkApp`.

The project is intentionally scoped as a **course-style capstone**: safe, explainable, non-diagnostic, and easy to extend.

---

## Architecture

The system is built around a root orchestrator agent and three specialized sub-agents:

- `report_insights_agent` — parses and summarizes medical reports into patient-friendly language and clinician, structured bullet points.
- `disease_monitor_agent` — takes time-stamped metrics (e.g. HbA1c, BP logs) and produces trend analysis & alerts.
- `scheduling_agent` — suggests follow-up schedules, simple reminders, and questions to ask the doctor.

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
