#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python3}"
venv_dir="${VENV_DIR:-.venv}"

if ! command -v "$python_bin" >/dev/null 2>&1; then
  echo "Missing $python_bin. Install Python 3.10+ and retry." >&2
  exit 1
fi

"$python_bin" -m venv "$venv_dir"

source "$venv_dir/bin/activate"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Ready: activated venv at $venv_dir"
echo "Next: source $venv_dir/bin/activate"

