from openai import RunHooks
from context import UserSessionContext

class MyRunHooks(RunHooks[UserSessionContext]):
    async def on_agent_start(self, agent, context, input):
        print(f"[HOOK] Agent started with input: {input}")

    async def on_tool_start(self, tool, context, input):
        print(f"[HOOK] Tool {tool.name} started with input: {input}")

    async def on_handoff(self, from_agent, to_agent, context):
        context.handoff_logs.append(f"Handoff from {from_agent.name} to {to_agent.name}")
