from openai import Tool

class GoalAnalyzerTool(Tool):
    name = "GoalAnalyzer"

    async def run(self, input, context):
        context.goal = {"target": "lose weight", "amount": 5, "duration": "2 months"}
        return "Understood goal: Lose 5kg in 2 months."
