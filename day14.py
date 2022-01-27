# Part 1: What do you get if you take the quantity of the most common element
# and subtract the quantity of the least common element?
import copy
from collections import Counter

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(rawData: str) -> tuple[str, list[tuple[str, str]]]:
    lines = rawData.splitlines()
    polymer = lines[0]
    data = []

    for item in lines[2:]:
        vals = item.split(" -> ")
        data.append((vals[0], vals[1]))

    return polymer, data


def get_score(poly: str) -> int:
    char_count: dict[str, int] = Counter()

    for char in poly:
        char_count[char] += 1

    most_common = max(char_count.values())
    least_common = min(char_count.values())
    score = most_common - least_common

    return score


# Part 1
def form_polymers(rawData: str, steps: int) -> int:
    polymer, data = parse_input(rawData)

    for _ in range(steps):
        polymer_copy = copy.deepcopy(polymer)

        for inst in data:
            new_val = f"{inst[0]}{inst[1]}"
            polymer_copy.replace(inst[0], new_val)

        polymer = polymer_copy

    score = get_score(polymer)
    return score


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = form_polymers(rawData, 10)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day14.txt"))
    raise SystemExit(main("input_sri/day14.txt"))


# Tests
test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "steps", "expected"),
    [
        (test_data, 10, 1588),
    ],
)
def test_form_polymers(input_data, steps, expected):
    assert form_polymers(input_data, steps) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data: list[int], expected: int) -> None:
    assert f(input_data) == expected
"""
