from openai import Agent
from context import UserSessionContext

escalation_agent = Agent(
    name="EscalationAgent",
    instructions="Escalate to human support when requested."
)