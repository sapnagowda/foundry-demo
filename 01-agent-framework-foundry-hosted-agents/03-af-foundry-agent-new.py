"""
Foundry Agent Service (classic) quickstart-style client.

Key point:
- The agent + thread + run live in Foundry Agent Service.
- This script is still the *client/orchestrator* that drives those API calls.
"""

import os
from dotenv import load_dotenv

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import CodeInterpreterTool  # optional tool example

load_dotenv()

def main() -> None:
    # Use the *Foundry project endpoint* (classic doc calls this PROJECT_ENDPOINT)
    # Format: https://<AIFoundryResourceName>.services.ai.azure.com/api/projects/<ProjectName>
    project_endpoint = os.getenv("PROJECT_ENDPOINT") or os.getenv("AZURE_AI_PROJECT_ENDPOINT")
    if not project_endpoint:
        raise ValueError("Missing PROJECT_ENDPOINT (or AZURE_AI_PROJECT_ENDPOINT).")

    # Use the *project deployment name* (classic doc calls this MODEL_DEPLOYMENT_NAME)
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME") or os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    if not model_deployment:
        raise ValueError("Missing MODEL_DEPLOYMENT_NAME (or AZURE_OPENAI_DEPLOYMENT_NAME).")

    # DefaultAzureCredential will work locally (Azure CLI), and also in Azure (Managed Identity)
    credential = DefaultAzureCredential()

    # This client talks to the Foundry Agent Service endpoint (classic).
    project_client = AIProjectClient(endpoint=project_endpoint, credential=credential)

    with project_client:
        # Optional: attach built-in tool(s) that execute in the service.
        code_interpreter = CodeInterpreterTool()

        # Create agent in the service
        agent = project_client.agents.create_agent(
            model=model_deployment,
            name="Quickstart",
            instructions="Be concise.",
            tools=code_interpreter.definitions,
            tool_resources=code_interpreter.resources,
        )
        print(f"Created agent: {agent.id}")

        # Create thread in the service
        thread = project_client.agents.threads.create()
        print(f"Created thread: {thread.id}")

        # Create message in the service
        project_client.agents.messages.create(
            thread_id=thread.id,
            role="user",
            content="Write a haiku about Azure AI Foundry.",
        )

        # Create + process run in the service (server-side execution)
        run = project_client.agents.runs.create_and_process(
            thread_id=thread.id,
            agent_id=agent.id,
        )
        print(f"Run status: {run.status}")

        # Fetch conversation from the service
        messages = project_client.agents.messages.list(thread_id=thread.id)
        for m in messages:
            # Message content is structured; print the raw for now
            print(f"{m.role}: {m.content}")

        # Cleanup (optional)
        # project_client.agents.delete_agent(agent.id)
        # project_client.agents.threads.delete(thread.id)

if __name__ == "__main__":
    main()
