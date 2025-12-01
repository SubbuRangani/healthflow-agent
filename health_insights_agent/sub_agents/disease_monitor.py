    """Sub-agent for interpreting time-series disease metrics."""

    from google.adk.agents import LlmAgent
    from .. import config
    from .. import tools


    disease_monitor_agent = LlmAgent(
        name="disease_monitor_agent",
        model=config.DEFAULT_MODEL,
        description=(
            "Interprets time-series metrics for chronic diseases (e.g., diabetes, "
            "hypertension) and gives non-diagnostic trend insights."
        ),
        instruction=(
            "You receive structured time-series health metrics from tools or user input. "
            "Examples: HbA1c over time, blood pressure logs, weight trends.

"
            "Your tasks:
"
            "1. Identify simple trends (improving, worsening, stable).
"
            "2. Comment on adherence (e.g., 'many readings are missing').
"
            "3. Suggest general lifestyle questions the patient may discuss with a doctor "
            "   (e.g., diet, exercise, medication adherence). Do NOT prescribe.
"
            "4. Encourage follow-up appointments if trends look concerning.
"
        ),
        tools=[
            tools.get_patient_record,
            tools.upsert_patient_record,
        ],
    )
