"""Foundations package: small examples of Python basics."""

from .utils import greet, factorial, top_n
from .models import Person
from .io_helpers import read_lines, write_lines

__all__ = ["greet", "factorial", "top_n", "Person", "read_lines", "write_lines"]
