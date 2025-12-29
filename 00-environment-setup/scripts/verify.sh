#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

echo "Verifying local environment..."

command -v az >/dev/null 2>&1 || fail "Azure CLI (az) not found"
command -v azd >/dev/null 2>&1 || fail "Azure Developer CLI (azd) not found"
command -v python3 >/dev/null 2>&1 || fail "python3 not found"

echo "- az: $(az version --query '\"azure-cli\"' -o tsv 2>/dev/null || echo ok)"
echo "- azd: $(azd version 2>/dev/null | head -n 1 || echo ok)"
echo "- python3: $(python3 --version)"

echo "Checking Azure login..."
az account show >/dev/null 2>&1 || fail "Not logged in. Run: az login"
echo "- az account show: ok"

if [ -f ".venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source ".venv/bin/activate"
fi

python3 -m pip --version >/dev/null 2>&1 || fail "pip not available for python3"

if [ -f "requirements.txt" ]; then
  python3 -m pip install -r requirements.txt >/dev/null
  echo "- python deps: ok"
fi

echo "OK"

