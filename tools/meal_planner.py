from openai import Tool

class MealPlannerTool(Tool):
    name = "MealPlanner"

    async def run(self, input, context):
        context.meal_plan = ["Day 1: Oats", "Day 2: Salad", "..."]
        return "Generated a 7-day vegetarian meal plan."