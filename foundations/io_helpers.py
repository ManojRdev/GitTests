"""Helpers for simple file I/O and context manager usage."""
from typing import List


def read_lines(path: str) -> List[str]:
    """Read a text file and return list of stripped lines."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def write_lines(path: str, lines: List[str]) -> None:
    """Write a list of strings to a file, one per line."""
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")
