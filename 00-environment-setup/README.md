# 00 — Environment Setup

## Goal
Establish a repeatable local environment for the workshop (Python runtime, Azure CLIs, and baseline configuration) so every later step is runnable and traceable.

## You will end with
- A working Python environment for local agent runs
- `az` + `azd` installed and authenticated
- A `.env` file populated with the values used in later steps (kept out of git)

## Prerequisites
- Azure subscription with permission to create resources (Foundry, App Insights, APIM, Logic Apps, Search)

## Install tooling
- Azure CLI (`az`): install via your preferred method for your OS.
- Azure Developer CLI (`azd`) (required for deploying hosted agents):
  - `brew tap azure/azd && brew install azd`
- Python: 3.10+ recommended.

## Create a virtual environment
If you prefer the manual approach:
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python -m pip install --upgrade pip`

Or use the provided bootstrap script (creates `.venv/` and installs dependencies):
- `bash 00-environment-setup/scripts/bootstrap_venv.sh`

## Install Python dependencies
This repo pins its Python dependencies in `requirements.txt` (including `openai`, `agent_framework`, and `python-dotenv`):
- `python -m pip install -r requirements.txt`

## Configure environment variables
- Copy `00-environment-setup/.env.example` → `.env` (repo root) and populate values as you reach steps that need them.

## Verify
- `bash 00-environment-setup/scripts/verify.sh`

## Proof (checklist)
- [ ] `az account show` returns the intended subscription
- [ ] `azd version` prints successfully
- [ ] `python3 --version` is 3.10+
- [ ] `pip install -r requirements.txt` succeeds

## Next
Continue to `../01-foundry-project-and-model-deployment`.

---

**Author:** Ozgur Guler | AI Solution Leader, AI Innovation Hub | [ozgur.guler1@gmail.com](mailto:ozgur.guler1@gmail.com)
© 2025 Ozgur Guler. All rights reserved.
