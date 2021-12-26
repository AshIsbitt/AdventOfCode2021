# Part 1: Determine the horizontal position that the crabs can align to using
# the least fuel possible. How much fuel must they spend to align to that
# position?
import pytest


def crab_Alignment(data: list[int]) -> int:
    fuel_Count = 0

    return fuel_Count


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    split_data = []
    split_data = rawData.split(",")

    # Convert to ints
    data = list(map(int, split_data))

    print(f"Part 1: {crab_Alignment(data)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day07.txt"))
    # raise SystemExit(main('input_sri/day07.txt'))


# Tests
test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 37),))
def test_crab_Alignment(input_data: list[int], expected: int) -> None:
    assert crab_Alignment(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
