# 01 — Agent Framework Agent (Local “Hello Agent”)

This step is intentionally “boring”: a minimal Microsoft Agent Framework agent that runs on your own compute and calls an Azure-hosted model over HTTPS. That baseline is what makes every later platform capability provable.

## Agents in Azure AI Foundry: Execution Models Explained

![Foundry Agent Service overview diagram](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/media/agent-service-the-glue.png?view=foundry-classic)

![Foundry private network isolation diagram](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/media/private-network-isolation.png?view=foundry-classic)

![Containerized agents illustration](https://rios.engineer/wp-content/uploads/2024/03/ado-agent-aci-feature.png)

This repository intentionally demonstrates **three distinct agent execution models** that coexist in Azure AI Foundry today. They are not incremental variations of the same thing — they represent **different levels of control over the agent runtime**.

Understanding this distinction is critical to understanding *why* Foundry Agent Service, Agent ID, MCP, and workflows now work the way they do.

---

## 1. Agent Framework Agent (Local Compute, API-Driven)

**What it is**

A traditional, code-defined agent built using **Microsoft Agent Framework**, running on **your own compute** (laptop, VM, container, CI runner).

**Characteristics**

- You own:
  - process lifecycle
  - dependencies
  - execution environment
- Azure provides:
  - model endpoints
  - tracing backends
  - identity primitives (optionally)
- The agent calls Azure OpenAI / Foundry models **over HTTPS**

**Mental model**

> An agent is an application you run, that happens to call Azure-hosted models.

**Why this matters**

This is the **baseline**. It proves:

- the agent logic
- tool calling
- reasoning behavior
- trace emission

before *any* platform abstraction is introduced.

**Where in this repo**

`01-agent-framework-agent/`

This step is intentionally boring — and that’s the point.

---

## 2. Foundry Agent Service Agent (Managed Runtime, Non-Containerized)

**What it is**

An agent defined *in code*, but executed **inside the Foundry Agent Service runtime** — **without containerization**.

This is what most people historically meant by “Foundry agents”.

**Characteristics**

- Azure manages:
  - execution runtime
  - scaling
  - lifecycle
- You define:
  - agent identity
  - instructions
  - tools
  - grounding
- You **do not deploy software**
- You **cannot bring arbitrary dependencies**
- Execution happens in a **shared, opaque service**

**Mental model**

> An agent is a configured inference behavior inside Azure.

**Limitations (by design)**

- No custom runtime
- No system-level control
- No deterministic lifecycle
- Limited observability boundaries

This model is powerful for **configuration-first agents**, but it is not suitable for:

- enterprise workflows
- regulated environments
- agent-to-agent composition
- MCP tool servers

**Why it still exists**

Because it offers:

- zero-ops onboarding
- fast experimentation
- strong UX abstraction

**Where this shows up**

This repo treats this model as an **intermediate abstraction**, not the end state.

---

## 3. Foundry Agent Service — Hosted Agents (Containerized, Code-First)

Hosted Agents are not just “better agents”.
They are a **new execution substrate**.

**What changed**

Foundry agents are now:

- containerized
- code-defined
- versioned artifacts
- identity-bearing workloads
- schedulable compute

Azure did not just add a feature — it **replaced the execution model**.

**Mental model**

> An agent is a deployed application that speaks the Foundry Agent protocol.

This aligns agents with:

- Azure Functions
- App Service
- Containers
- Kubernetes workloads

…but purpose-built for:

- conversations
- tool calling
- MCP
- agent identity
- governance

**Why containerization is the hard boundary**

Once agents are containers, the platform can finally provide:

- stable Agent IDs
- Conditional Access enforcement
- deterministic observability
- MCP tool consumption *and* exposure
- agent-to-agent workflows
- lifecycle management (deploy, version, rollback)

None of this is reliable without containers.

**Where in this repo**

`04-azd-deploy-hosted-agent/`

This step shows:

- how the same agent logic becomes a **deployable workload**
- how Foundry becomes a **control plane**, not a runtime black box

---

## How This Repo Is Structured (On Purpose)

This repository is linear because the platform evolution is linear.

| Step | What you learn | Why it exists |
| --- | --- | --- |
| 01 | Agent logic in isolation | Prove behavior |
| 02–03 | Observability + model wiring | Prove signals and endpoints |
| 04 | Hosted Agent deployment | Cross the container boundary |
| 05+ | Identity, MCP, workflows | Use the new substrate |

Each step answers one question:

> What becomes possible *only* after this execution model exists?

---

## Key takeaway

The real evolution is not “hosted vs non-hosted agents”.

It is:

> From prompt-defined agents → containerized, code-first agent workloads

Everything else — Agent ID, MCP, A2A workflows, governance — is downstream of that single architectural change.

This repo is built to make that undeniable.

---

## Run locally

Prereqs:
- Complete `00-environment-setup/` and create `.env` from `00-environment-setup/.env.example`
- Ensure `.env` includes `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_VERSION`, and a deployment name

Commands:
- `python3 01-agent-framework-agent/agent/hello_agent.py`
- `python3 01-agent-framework-agent/agent/hello_agent_reasoning_min.py`

## Proof (checklist)

- [ ] Agent runs locally and returns a model response
- [ ] Environment variables load from `.env`

## Next

Continue to `../02-observability-otel-to-appinsights`.
