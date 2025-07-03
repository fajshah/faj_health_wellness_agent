from openai import Agent
from context import UserSessionContext

injury_support_agent = Agent(
    name="InjurySupportAgent",
    instructions="Help users with physical limitations or injury-related plans."
)