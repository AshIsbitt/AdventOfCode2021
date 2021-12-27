# Part 1: Determine the horizontal position that the crabs can align to using
# the least fuel possible. How much fuel must they spend to align to that
# position?
# Part 2: As it turns out, crab submarine engines don't burn fuel at a constant
# rate. How much fuel must they spend to align to that position?
import math

import pytest


def crab_Alignment(data: list[int]) -> int:
    fuel_Count = 0

    data.sort()
    median = data[len(data) // 2]

    for item in data:
        fuel_Count += abs(item - median)

    return fuel_Count


def exponential_crab_alignment(data: list[int]) -> int:
    fuel_count = 0

    data.sort()
    # In this case, it's the mean +- 1
    mean = int(sum(data) / len(data))  # If this doesn't work, use the one below
    # mean = math.ceil(sum(data) / len(data))

    for item in data:
        values = abs(mean - item)

        for elem in range(values):
            fuel_count += elem + 1

    return fuel_count


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    split_data = []
    split_data = rawData.split(",")

    # Convert to ints
    data = list(map(int, split_data))

    print(f"Part 1: {crab_Alignment(data)}")
    print(f"Part 2: {exponential_crab_alignment(data)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day07.txt"))
    # raise SystemExit(main("input_sri/day07.txt"))


# Tests
test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 37),))
def test_crab_Alignment(input_data: list[int], expected: int) -> None:
    assert crab_Alignment(input_data) == expected


# Part 2 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 168),))
def test_exponential_crab_alignment(input_data: list[int], expected: int) -> None:
    assert exponential_crab_alignment(input_data) == expected
