# Part 1: Given the starting energy levels of the dumbo octopuses in your
# cavern, simulate 100 steps. How many total flashes are there after 100 steps?
import pprint as p
from typing import Generator

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(rawData: str) -> dict[tuple[int, int], int]:
    data = {}

    for x, line in enumerate(rawData.splitlines()):
        for y, val in enumerate(line):
            data[(x, y)] = int(val)

    return data


def detect_flash(data: dict[tuple[int, int], int], coords: tuple[int, int]) -> bool:
    r, c = coords
    return True if data[(r, c)] == 10 else False


def surroundings(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield (x - 1, y - 1)
    yield (x - 1, y)
    yield (x - 1, y + 1)
    yield (x, y - 1)
    yield (x, y + 1)
    yield (x + 1, y - 1)
    yield (x + 1, y)
    yield (x + 1, y + 1)


def check_surroundings(
    data: dict[tuple[int, int], int], coords: tuple[int, int]
) -> tuple[dict[tuple[int, int], int], int]:
    r, c = coords
    surrounding_flashes = 0

    for pt in surroundings(r, c):
        x, y = pt
        if x < 0 or y < 0:
            continue

        data[(x, y)] += 1

        if detect_flash(data, (x, y)):
            surrounding_flashes += 1

    return data, surrounding_flashes


# Part 1
def calculate_flashing_octopi(rawData: str, iterations: int) -> int:
    data: dict[tuple[int, int], int] = parse_input(rawData)
    flashes = 0

    for i in range(iterations):
        for coords, octo in data.items():
            r, c = coords
            data[(r, c)] += 1

            # Then, any octopus with an energy level greater than 9 flashes.
            if detect_flash(data, coords):
                flashes += 1

                ret = check_surroundings(data, coords)
                data = ret[0]
                flashes += ret[1]

        for coords, octo in data.items():
            if octo > 9:
                r, c = coords
                data[(r, c)] = 0

    return flashes


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData: str = inputData.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = calculate_flashing_octopi(rawData, 100)
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
test_data_1: str = """11111
19991
19191
19991
11111"""

test_data_2: str = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "iterations", "expected"),
    [
        (test_data_1, 3, 9),
        (test_data_2, 10, 204),
        (test_data_2, 100, 1656),
    ],
)
def test_calculate_flashing_octopi(
    input_data: str, iterations: int, expected: int
) -> None:
    assert calculate_flashing_octopi(input_data, iterations) == expected


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
