"""Minimal smoke test for Health Insights Agent.

This does **not** call the live Gemini model. It just ensures
the ADK graph can be instantiated without errors.
"""

from health_insights_agent.agent import root_agent


def test_root_agent_structure():
    assert root_agent.name == "health_insights_orchestrator"
    assert root_agent.sub_agents, "Root agent should have sub-agents configured."
