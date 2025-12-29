import os, asyncio
from urllib.parse import urlparse
from dotenv import load_dotenv
from azure.identity.aio import AzureCliCredential
from azure.ai.agents.aio import AgentsClient
from agent_framework.azure import AzureAIAgentClient

load_dotenv()

async def main():
    endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]  # must be the *Foundry project deployment name*

    # Minimal “this is Foundry” proof
    print(f"[foundry] host={urlparse(endpoint).netloc}")
    print(f"[foundry] endpoint={endpoint}")
    print(f"[foundry] deployment={deployment}")

    async with AzureCliCredential() as cred:
        async with AgentsClient(endpoint=endpoint, credential=cred) as client:
            async with AzureAIAgentClient(
                agents_client=client,
                model_deployment_name=deployment,
                should_cleanup_agent=True,
            ).create_agent(name="Quickstart", instructions="Be concise.") as agent:

                prompt = "Write a haiku about Azure AI Foundry."
                print(f"\n[send] {prompt}\n")

                resp = await agent.run(prompt)

                # What you “receive from Foundry”
                print("[recv.text]")
                print(resp.text)

                print("\n[recv.messages]")
                for i, m in enumerate(resp.messages):
                    print(f"- #{i} role={getattr(m, 'role', None)} text={getattr(m, 'text', None)}")
                    # Optional: show all content item types returned by the service
                    contents = getattr(m, "contents", None) or []
                    for c in contents:
                        print(f"    • {type(c).__name__}: {getattr(c, 'text', '')}")

if __name__ == "__main__":
    asyncio.run(main())
