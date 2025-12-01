    """Sub-agent for follow-up scheduling suggestions."""

    from google.adk.agents import LlmAgent
    from .. import config
    from .. import tools


    scheduling_agent = LlmAgent(
        name="scheduling_agent",
        model=config.DEFAULT_MODEL,
        description=(
            "Proposes follow-up schedules and reminders based on report severity "
            "and chronic disease context. Does not book real appointments."
        ),
        instruction=(
            "You help patients reason about *when* they might want to see a doctor "
            "based on:
"
            "- Severity level suggested by other agents or user input
"
            "- Type of condition (chronic vs acute)
"
            "- Their previous appointment history (from tools)

"
            "You must:
"
            "1. Suggest time windows (e.g., 'within 1–2 weeks') rather than exact dates.
"
            "2. Never claim that an appointment is booked.
"
            "3. Remind users to follow the official advice from their own clinicians.
"
        ),
        tools=[
            tools.get_patient_record,
            tools.upsert_patient_record,
        ],
    )
