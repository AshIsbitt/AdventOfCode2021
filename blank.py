# What to do
import pprint as p
from collections import counter
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


def main(filename: str) -> int:
    with open(filename) as input_data:
        raw_data = input_data.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = 0
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day01.txt"))
    raise SystemExit(main("input_sri/day01.txt"))


# Tests
test_data = """
"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ],
)
def test_f(input_data, expected):
    assert f(input_data) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data, expected):
    assert f(input_data) == expected
"""
