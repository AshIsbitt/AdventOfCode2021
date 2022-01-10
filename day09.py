# Part 1: Find all of the low points on your heightmap. What is the sum of the
# risk levels of all low points on your heightmap?
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


def parse_data(rawData: list[str]) -> list[list[int]]:
    data_map: list[list[int]] = []

    for item in rawData:
        row = [int(i) for i in item if i != "\n"]
        data_map.append(row)

    return data_map


def calculate_risk_level(rawData: list[str]) -> int:
    total_risk_lvl = 0
    data_map: list[list[int]] = parse_data(rawData)

    world_map = defaultdict(lambda: 9)

    for row, line in enumerate(data_map):
        for col, val in enumerate(line):
            world_map[(row, col)] = val

    # Turn it into a tuple to avoid a runtimeError
    for (x, y), n in tuple(world_map.items()):
        checks: list[bool] = []

        checks.append(True if world_map[(x + 1, y)] > n else False)
        checks.append(True if world_map[(x - 1, y)] > n else False)
        checks.append(True if world_map[(x, y + 1)] > n else False)
        checks.append(True if world_map[(x, y - 1)] > n else False)

        if all(checks):
            total_risk_lvl += 1 + n

    return total_risk_lvl


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = calculate_risk_level(rawData)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day09.txt"))
    raise SystemExit(main("input_sri/day09.txt"))


# Tests
test_data = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 15),
    ],
)
def test_calculate_risk_level(input_data: list[str], expected: int) -> None:
    assert calculate_risk_level(input_data) == expected


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
