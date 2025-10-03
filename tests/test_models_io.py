import os
from foundations.models import Person
from foundations.io_helpers import write_lines, read_lines


def test_person():
    p = Person("Bob", age=17)
    assert not p.is_adult()
    p.birthday()
    assert p.age == 18
    assert p.is_adult()


def test_io_helpers(tmp_path):
    p = tmp_path / "data.txt"
    lines = ["one", "two", "three"]
    write_lines(str(p), lines)
    read = read_lines(str(p))
    assert read == lines
