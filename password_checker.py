#!/usr/bin/env python3
import re
import string

RULES = {
    "length ≥ 8": lambda pw: len(pw) >= 8,
    "letter":      lambda pw: re.search(r"[A-Za-z]", pw),
    "number":      lambda pw: re.search(r"\d", pw),
    "symbol":      lambda pw: re.search(f"[{re.escape(string.punctuation)}]", pw),
}

def main() -> None:
    pw = input("Enter password: ")
    failed = [name for name, test in RULES.items() if not test(pw)]
    if not failed:
        print("✅ Strong password!")
    else:
        print("❌ Weak password. Missing:", ", ".join(failed))

if __name__ == "__main__":
    main()