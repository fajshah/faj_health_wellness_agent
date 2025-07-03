from openai import Tool

class CheckinSchedulerTool(Tool):
    name = "CheckinScheduler"

    async def run(self, input, context):
        return "Scheduled weekly progress check-ins."