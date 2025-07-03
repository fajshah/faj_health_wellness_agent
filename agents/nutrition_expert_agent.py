from openai import Agent
from context import UserSessionContext

nutrition_expert_agent = Agent(
    name="NutritionExpertAgent",
    instructions="Handle complex dietary needs like diabetes or allergies."
)