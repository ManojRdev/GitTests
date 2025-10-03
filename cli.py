"""Tiny CLI demonstrating package usage."""
import sys
from typing import List

from foundations import greet


def main(argv: List[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv or argv[0] in {"-h", "--help"}:
        print("Usage: python cli.py greet NAME")
        return 0
    cmd = argv[0]
    if cmd == "greet":
        if len(argv) < 2:
            print("Please provide a name")
            return 2
        print(greet(argv[1]))
        return 0
    print("Unknown command")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
