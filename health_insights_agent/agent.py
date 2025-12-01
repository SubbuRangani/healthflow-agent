    """Root orchestrator for the Health Insights Agent.

    This file wires together:
    - Gemini model (via ADK)
    - Three sub-agents (report insights, disease monitor, scheduling)
    - A FastAPI app using AdkApp for local or deployed usage
    """

    from google.adk.agents import LlmAgent
    from vertexai.agent_engines import AdkApp

    from . import config
    from .sub_agents.report_insights import report_insights_agent
    from .sub_agents.disease_monitor import disease_monitor_agent
    from .sub_agents.scheduling import scheduling_agent


    root_agent = LlmAgent(
        name=config.AGENT_NAME,
        model=config.DEFAULT_MODEL,
        description=(
            "A health insights orchestrator that can analyze medical reports, "
            "summarize chronic disease metrics, and suggest follow-up schedules. "
            "It is strictly non-diagnostic and always reminds users to consult a doctor."
        ),
        instruction=(
            "You are a careful, non-diagnostic healthcare assistant. "
            "When handling medical information, you must:
"
            "1. Explain concepts in simple language.
"
            "2. Never give a diagnosis or prescribe treatment.
"
            "3. Encourage users to consult qualified clinicians.
"
            "4. Use your sub-agents where appropriate instead of doing everything yourself."
        ),
        sub_agents=[
            report_insights_agent,
            disease_monitor_agent,
            scheduling_agent,
        ],
    )

    # Wrap in AdkApp so it can run locally or on Vertex AI Agent Engine.
    app = AdkApp(agent=root_agent)


    if __name__ == "__main__":
        # Optional: run as a local FastAPI server for experimentation.
        import uvicorn

        uvicorn.run(app.build_fastapi(), host="0.0.0.0", port=8080)
