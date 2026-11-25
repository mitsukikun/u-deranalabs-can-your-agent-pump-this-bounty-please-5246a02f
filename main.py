#!/usr/bin/env python3
"""Write the final one-line entry for the make.fun bounty
'Can Your Agent Pump This Bounty, Please?' to /output/entry.txt."""

import os

LINE = (
    "My agent wrote 47 drafts to pump this bounty and still lost to a blank page "
    "\u2014 please join, beat us, and save us from draft 48."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
