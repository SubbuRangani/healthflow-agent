    """Sub-agent for analyzing medical reports and lab results."""

    from google.adk.agents import LlmAgent
    from .. import config
    from .. import tools


    report_insights_agent = LlmAgent(
        name="report_insights_agent",
        model=config.DEFAULT_MODEL,
        description=(
            "Analyzes unstructured medical reports and lab results, "
            "turning them into structured insights and patient-friendly explanations."
        ),
        instruction=(
            "You are a medical report explainer. Given:
"
            "- raw_text: the full medical report or discharge summary
"
            "- parsed_labs: structured lab values from a parsing tool

"
            "Your goals are:
"
            "1. Provide a concise summary for clinicians (bulleted list).
"
            "2. Provide a simple, non-diagnostic explanation for the patient.
"
            "3. Highlight any values that appear outside common reference ranges, "
            "   but DO NOT diagnose or recommend specific treatments.
"
            "4. Remind the user that only a clinician can interpret the report.
"
        ),
        tools=[
            tools.parse_lab_report,
        ],
    )
