from openai import Tool

class ProgressTrackerTool(Tool):
    name = "ProgressTracker"

    async def run(self, input, context):
        context.progress_logs.append({"day": "Day 1", "status": "Workout done"})
        return "Progress updated."
