#!/usr/bin/env python3
"""
Lightweight password checker + generator
----------------------------------------
• Validate passwords against 4 simple rules
• Batch-check a file or stdin
• Generate random strong passwords
"""

import argparse
import random
import re
import string
import sys
from typing import Iterable

MIN_LEN = 8
SYMBOLS = string.punctuation
RULES = {
    "length ≥ 8": lambda pw: len(pw) >= MIN_LEN,
    "letter":      lambda pw: re.search(r"[A-Za-z]", pw),
    "number":      lambda pw: re.search(r"\d", pw),
    "symbol":      lambda pw: re.search(f"[{re.escape(SYMBOLS)}]", pw),
}

# ---------- generator ----------
def make_password(length: int = 12) -> str:
    """Return a random password that meets all RULES."""
    while True:
        pw = "".join(random.choice(
            string.ascii_letters + string.digits + SYMBOLS
        ) for _ in range(length))
        if all(test(pw) for test in RULES.values()):
            return pw

# ---------- checker ----------
def evaluate(pw: str) -> tuple[bool, list[str]]:
    """Return (is_strong, missing_rules)."""
    missing = [name for name, test in RULES.items() if not test(pw)]
    return (not missing, missing)

# ---------- CLI ----------
def iter_passwords(args) -> Iterable[str]:
    if args.password:
        yield args.password
    elif args.file:
        with open(args.file, encoding="utf-8") as f:
            for line in f:
                pw = line.rstrip("\n")
                if pw:
                    yield pw
    else:                              
        for line in sys.stdin:
            pw = line.rstrip("\n")
            if pw:
                yield pw

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check or generate secure passwords")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("-p", "--password", help="password to check")
    g.add_argument("-f", "--file",     help="newline-separated passwords file")
    g.add_argument("-g", "--generate", type=int, nargs="?", const=12,
                   metavar="LEN", help="generate a strong password (default 12)")
    args = parser.parse_args()

    if args.generate is not None:                       
        print(make_password(args.generate))
        return

    for pw in iter_passwords(args):
        strong, missing = evaluate(pw)
        if strong:
            print(f"✅  '{pw}'  is STRONG")
        else:
            print(f"❌  '{pw}'  missing: {', '.join(missing)}")

if __name__ == "__main__":
    main()
