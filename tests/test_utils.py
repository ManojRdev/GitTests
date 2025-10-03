import os
from foundations import greet, factorial, top_n


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_top_n():
    assert top_n([1, 5, 3, 2], 2) == [5, 3]
