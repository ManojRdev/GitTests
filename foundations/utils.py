"""Utility functions demonstrating typing, errors, and recursion."""
from typing import List


def greet(name: str) -> str:
    """Return a greeting for name.

    Args:
        name: Person's name.

    Returns:
        Greeting string.
    """
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


def factorial(n: int) -> int:
    """Compute factorial iteratively with input validation.

    Args:
        n: non-negative integer

    Returns:
        n! as int
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def top_n(items: List[int], n: int = 3) -> List[int]:
    """Return the top n largest items sorted descending."""
    return sorted(items, reverse=True)[:n]


def _private_function() -> None:
    """This function is private and should not be imported."""
    pass
