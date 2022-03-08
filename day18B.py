# Part 1: Add up all of the snailfish numbers from the homework assignment in
# the order they appear. What is the magnitude of the final sum?
import ast
import pprint as p
from collections import Counter
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


# Part 1
def calculate_homework(data: list[object]) -> int:
    final_val = 0
    return final_val


def main(filename: str) -> int:
    raw_data: list[object] = []

    with open(filename) as input_data:
        lines = input_data.readlines()
        for line in lines:
            raw_data.append(ast.literal_eval(line))

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = calculate_homework(raw_data)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day18.txt"))
    raise SystemExit(main("input_sri/day18.txt"))


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
def test_calculate_homework(input_data, expected):
    assert calculate_homework(input_data) == expected


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
