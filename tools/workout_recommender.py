from openai import Tool

class WorkoutRecommenderTool(Tool):
    name = "WorkoutRecommender"

    async def run(self, input, context):
        context.workout_plan = {"Mon": "Cardio", "Tue": "Strength"}
        return "Here is your weekly workout plan."