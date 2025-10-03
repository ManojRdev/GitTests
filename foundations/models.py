"""Simple data models using dataclasses."""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int = 0

    def birthday(self) -> None:
        """Increment age by one."""
        self.age += 1

    def is_adult(self) -> bool:
        return self.age >= 18
