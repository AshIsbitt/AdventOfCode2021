# Part 1: Given the starting energy levels of the dumbo octopuses in your
# cavern, simulate 100 steps. How many total flashes are there after 100 steps?
import pyperclip as pyp  # type: ignore
import pytest


def parse_input(rawData: str) -> list[list[int]]:
    pass


def calculate_flashing_octopi(rawData: str, iterations: int) -> int:
    data = parse_input(rawData)
    print(data)

    flashes: int = 0

    return flashes


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

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
    input_data: list[int], iterations: int, expected: int
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
