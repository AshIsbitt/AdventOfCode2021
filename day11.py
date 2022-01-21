# Part 1: Given the starting energy levels of the dumbo octopuses in your
# cavern, simulate 100 steps. How many total flashes are there after 100 steps?
# Part 2: What is the first step during which all octopuses flash?
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
    x, y = coords
    return True if data[x, y] > 9 else False


def surroundings(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield (x - 1, y - 1)
    yield (x - 1, y)
    yield (x - 1, y + 1)
    yield (x, y - 1)
    yield (x, y + 1)
    yield (x + 1, y - 1)
    yield (x + 1, y)
    yield (x + 1, y + 1)


# Part 1
def calculate_flashing_octopi(rawData: str, iterations: int) -> int:
    data = parse_input(rawData)
    flashes = 0

    for i in range(iterations):
        flashing_octos = set()
        flashes_per_iter = 0

        for coords, octo in data.items():
            x, y = coords
            data[x, y] += 1

            if detect_flash(data, coords):
                flashing_octos.add(coords)

        while flashing_octos:
            coord = flashing_octos.pop()
            data[coord] = -15
            flashes_per_iter += 1

            x, y = coord
            for pt in surroundings(x, y):
                try:
                    data[pt] += 1
                except KeyError:
                    continue

                if detect_flash(data, pt):
                    flashing_octos.add(pt)

        for coords, octo in data.items():
            if octo < 0:
                r, c = coords
                data[(r, c)] = 0

        flashes += flashes_per_iter

    return flashes


# Part 2
def find_sync_point(rawData: str) -> int:
    data = parse_input(rawData)

    step = 0
    in_sync = False

    while not in_sync:
        print(data)
        pass

    return step


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

    p2 = find_sync_point(rawData)
    pyp.copy(p2)
    print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day11.txt"))
    raise SystemExit(main("input_sri/day11.txt"))


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
        (test_data_1, 2, 9),
        (test_data_2, 2, 35),
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
