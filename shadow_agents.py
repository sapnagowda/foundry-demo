#!/usr/bin/env python3
"""
Shadow Agents - Intro Sequence
Synced to narration: "Shadow agents are already live..."
Duration: 10-12 seconds

SCRIPT:
  2s - org context (blurred Teams/portal)
  3s - terminal run (shadow agent)
  3s - helpful output (works/useful)
  2s - "touching systems"
  2s - risk stamps → INCIDENT PRONE
"""

import time
import sys
import os

# Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
WHITE = "\033[97m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"
BG_RED = "\033[41m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ═══════════════════════════════════════════════════════════════════
# 2s - ORG CONTEXT (blurred portal/Teams vibe)
# Narration: "Shadow agents are already live..."
# ═══════════════════════════════════════════════════════════════════
def org_context():
    print(f"""
{DIM}
    ┌────────────────────────────────────────────────────────────┐
    │  ▓▓▓▓▓▓▓▓▓▓  │  ████████  │  ▒▒▒▒▒▒▒▒  │  ░░░░░░░░░░░░░  │
    ├────────────────────────────────────────────────────────────┤
    │                                                            │
    │    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ████████████████     ░░░░░░░░░░   │
    │    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ████████████████     ░░░░░░░░░░   │
    │                                                            │
    │    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ████████████ │
    │    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ████████████ │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
{RESET}""")
    print(f"  {DIM}Somewhere in your organization...{RESET}")
    time.sleep(2)

# ═══════════════════════════════════════════════════════════════════
# 3s - TERMINAL RUN (shadow agent starting)
# Narration: "...an agent is already running outside governance."
# ═══════════════════════════════════════════════════════════════════
def terminal_run():
    clear()
    print(f"\n{DIM}  $ python agent.py{RESET}\n")
    time.sleep(0.4)

    steps = [
        "Initializing agent...",
        "Connected to gpt-4o",
        "Tools loaded: [email, calendar, database]",
        "Agent ready.",
    ]

    for step in steps:
        print(f"  {GREEN}✓{RESET} {step}")
        time.sleep(0.5)

    time.sleep(0.4)

# ═══════════════════════════════════════════════════════════════════
# 3s - HELPFUL OUTPUT (it works, it's useful)
# Narration: "It works. It's useful."
# ═══════════════════════════════════════════════════════════════════
def helpful_output():
    print(f"\n{DIM}  ─────────────────────────────────────────────────────{RESET}")
    print(f"  {CYAN}USER:{RESET} Summarize my emails and schedule follow-ups")
    print(f"{DIM}  ─────────────────────────────────────────────────────{RESET}\n")
    time.sleep(0.5)

    print(f"  {DIM}Reading inbox...{RESET}")
    time.sleep(0.5)
    print(f"  {DIM}Processing 14 messages...{RESET}")
    time.sleep(0.5)

    print(f"\n  {GREEN}AGENT:{RESET} Done. 3 follow-ups scheduled:")
    print(f"  {WHITE}  • Q3 review → tomorrow 2pm{RESET}")
    print(f"  {WHITE}  • Client call → Thursday{RESET}")
    print(f"  {WHITE}  • Team sync → Friday{RESET}")
    time.sleep(0.8)

    print(f"\n  {GREEN}{BOLD}It works. It's useful.{RESET}")
    time.sleep(0.5)

# ═══════════════════════════════════════════════════════════════════
# 2s - TOUCHING SYSTEMS (the turn)
# Narration: "And the moment it touches real systems..."
# ═══════════════════════════════════════════════════════════════════
def touching_systems():
    print(f"\n{DIM}  ─────────────────────────────────────────────────────{RESET}")
    print(f"  {YELLOW}And the moment it touches real systems...{RESET}\n")
    time.sleep(0.4)

    # Split screen effect
    print(f"  ┌─────────────────────────┬─────────────────────────┐")
    print(f"  │ {GREEN}AGENT OUTPUT{RESET}            │ {RED}OBSERVABILITY{RESET}           │")
    print(f"  ├─────────────────────────┼─────────────────────────┤")
    print(f"  │ {GREEN}✓{RESET} Task completed        │ {RED}No trace ID{RESET}             │")
    print(f"  │ {GREEN}✓{RESET} Emails accessed       │ {RED}No agent identity{RESET}       │")
    print(f"  │ {GREEN}✓{RESET} Calendar modified     │ {RED}No audit log{RESET}            │")
    print(f"  │ {GREEN}✓{RESET} External email sent   │ {RED}No policy check{RESET}         │")
    print(f"  └─────────────────────────┴─────────────────────────┘")
    time.sleep(1.2)

    print(f"\n  {RED}{BOLD}...it becomes a risk.{RESET}")
    time.sleep(0.4)

# ═══════════════════════════════════════════════════════════════════
# 2s - RISK STAMPS (rapid fire → final stamp)
# Goal: dread + inevitability
# ═══════════════════════════════════════════════════════════════════
def risk_stamps():
    print()

    stamps = [
        " ██ NO IDENTITY ██ ",
        " ██ NO POLICY GATE ██ ",
        " ██ NO AUDIT TRAIL ██ ",
    ]

    for stamp in stamps:
        print(f"  {BG_RED}{WHITE}{BOLD}{stamp}{RESET}")
        time.sleep(0.3)

    time.sleep(0.2)

    # Final stamp
    print(f"""
  {BG_RED}{WHITE}{BOLD}
  ╔═══════════════════════════════════════╗
  ║                                       ║
  ║       ⚠️  INCIDENT PRONE  ⚠️           ║
  ║                                       ║
  ╚═══════════════════════════════════════╝
  {RESET}""")
    time.sleep(0.8)

# ═══════════════════════════════════════════════════════════════════
# TRANSITION
# ═══════════════════════════════════════════════════════════════════
def transition():
    print(f"\n{CYAN}{BOLD}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"\n  {GREEN}{BOLD}Let's fix that.{RESET}")
    print(f"  {GREEN}Azure AI Foundry — Enterprise Agent Governance{RESET}\n")

# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════
def main():
    clear()

    org_context()        # 2s - blurred org context
    terminal_run()       # 3s - shadow agent starts
    helpful_output()     # 3s - works/useful
    touching_systems()   # 2s - split screen + "becomes a risk"
    risk_stamps()        # 2s - stamps → INCIDENT PRONE
    transition()         # transition out

if __name__ == "__main__":
    main()
