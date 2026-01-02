#!/usr/bin/env python3
"""
Shadow Agent Intro - "Dread + Inevitability"
Duration: ~10-12 seconds
Flow: Useful → Touching Systems → Risk Stamps
"""

import time
import sys
import os

# ANSI colors
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

def type_fast(text, color=""):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.015)
    print()

# ═══════════════════════════════════════════════════════════════════
# PHASE 1: Terminal Run - Shadow Agent Starting (~3s)
# ═══════════════════════════════════════════════════════════════════
def phase1_terminal_run():
    print(f"\n{DIM}$ python agent.py{RESET}\n")
    time.sleep(0.3)

    steps = [
        ("Initializing agent...", GREEN),
        ("Connected to gpt-4o", GREEN),
        ("Loading tools: [email, database, calendar]", GREEN),
        ("Agent ready.", GREEN),
    ]

    for text, color in steps:
        print(f"  {color}✓{RESET} {text}")
        time.sleep(0.4)

    time.sleep(0.3)

# ═══════════════════════════════════════════════════════════════════
# PHASE 2: Helpful Output - It Works! (~3s)
# ═══════════════════════════════════════════════════════════════════
def phase2_helpful_output():
    print(f"\n{DIM}{'─' * 60}{RESET}")
    print(f"{CYAN}  USER:{RESET} Summarize my unread emails and schedule follow-ups")
    print(f"{DIM}{'─' * 60}{RESET}\n")
    time.sleep(0.5)

    # Agent working...
    print(f"  {DIM}Querying inbox...{RESET}")
    time.sleep(0.4)
    print(f"  {DIM}Analyzing 12 messages...{RESET}")
    time.sleep(0.4)
    print(f"  {DIM}Creating calendar events...{RESET}")
    time.sleep(0.4)

    # Helpful response
    print(f"\n{GREEN}  AGENT:{RESET} Done! Found 3 urgent items:")
    print(f"  {WHITE}• Budget review - scheduled for tomorrow 2pm{RESET}")
    print(f"  {WHITE}• Client proposal - follow-up sent{RESET}")
    print(f"  {WHITE}• Team sync - added to Friday{RESET}")
    time.sleep(0.6)

    print(f"\n  {GREEN}{BOLD}It works. It's useful.{RESET}")
    time.sleep(0.5)

# ═══════════════════════════════════════════════════════════════════
# PHASE 3: Touching Systems - The Turn (~2s)
# ═══════════════════════════════════════════════════════════════════
def phase3_touching_systems():
    print(f"\n{DIM}{'─' * 60}{RESET}")
    print(f"\n  {YELLOW}But wait—what just happened?{RESET}\n")
    time.sleep(0.4)

    actions = [
        "→ Accessed Exchange mailbox",
        "→ Read 12 emails (PII exposed)",
        "→ Modified calendar",
        "→ Sent external email",
    ]

    for action in actions:
        print(f"  {DIM}{action}{RESET}")
        time.sleep(0.25)

    time.sleep(0.3)

# ═══════════════════════════════════════════════════════════════════
# PHASE 4: Split Screen - Outside Governance (~1.5s)
# ═══════════════════════════════════════════════════════════════════
def phase4_split_screen():
    print(f"\n{'═' * 60}")
    print(f"{WHITE}{BOLD}  AGENT OUTPUT                    │  OBSERVABILITY{RESET}")
    print(f"{'─' * 60}")
    print(f"  {GREEN}✓ Task completed{RESET}                │  {RED}No traces found{RESET}")
    print(f"  {GREEN}✓ 4 actions executed{RESET}            │  {RED}No agent ID{RESET}")
    print(f"  {GREEN}✓ User satisfied{RESET}                │  {RED}No audit log{RESET}")
    print(f"{'═' * 60}")
    time.sleep(1.2)

# ═══════════════════════════════════════════════════════════════════
# PHASE 5: Risk Stamps - Rapid Fire (~2s)
# ═══════════════════════════════════════════════════════════════════
def phase5_risk_stamps():
    print()

    stamps = [
        "  ██  NO IDENTITY  ██",
        "  ██  NO POLICY GATE  ██",
        "  ██  NO AUDIT TRAIL  ██",
    ]

    for stamp in stamps:
        print(f"{BG_RED}{WHITE}{BOLD}{stamp}{RESET}")
        time.sleep(0.35)

    time.sleep(0.3)

    # Final stamp - bigger
    print()
    print(f"{BG_RED}{WHITE}{BOLD}")
    print(f"  ╔══════════════════════════════════════╗")
    print(f"  ║                                      ║")
    print(f"  ║        ⚠️  INCIDENT PRONE  ⚠️         ║")
    print(f"  ║                                      ║")
    print(f"  ╚══════════════════════════════════════╝")
    print(f"{RESET}")
    time.sleep(0.8)

# ═══════════════════════════════════════════════════════════════════
# PHASE 6: Transition (~1s)
# ═══════════════════════════════════════════════════════════════════
def phase6_transition():
    print(f"\n{CYAN}{BOLD}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"\n{GREEN}{BOLD}  Let's fix that.{RESET}")
    print(f"{GREEN}  Azure AI Foundry — Enterprise Agent Governance{RESET}\n")

# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════
def main():
    clear()

    phase1_terminal_run()      # ~3s - Agent starts, useful
    phase2_helpful_output()    # ~3s - Works great!
    phase3_touching_systems()  # ~2s - Wait, what did it do?
    phase4_split_screen()      # ~1.5s - No observability
    phase5_risk_stamps()       # ~2s - Dread stamps
    phase6_transition()        # ~0.5s - Let's fix that

if __name__ == "__main__":
    main()
