# Example Dockerfile for Health Insights Agent.
# This is a template and may need tweaks for your environment.

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the default port used in agent.py
EXPOSE 8080

# Run the FastAPI app via the AdkApp wrapper
CMD ["python", "-m", "health_insights_agent.agent"]
