from dotenv import load_dotenv
from agents import Agent, Runner, trace
from openai import AsyncAzureOpenAI
from agents import set_default_openai_client
from agents import set_tracing_export_api_key
import os
import asyncio

load_dotenv(override=True)

agent = Agent(
    name="Jokester",
    instructions="You are a joke teller",
    model="gpt-4.1-mini"
)

# openai_client = AsyncAzureOpenAI(
#     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#     api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
# )

# set_default_openai_client(openai_client)
# set_tracing_export_api_key(os.getenv("OPENAI_TRACING_EXPORT_API_KEY"))

async def main():
    with trace("Telling a joke"):
        result = await Runner.run(agent, "kể một câu chuyện cười về AI Automation Agent")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())