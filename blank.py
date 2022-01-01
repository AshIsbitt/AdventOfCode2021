# What to do
import pytest


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()
    rawData = [line.rstrip("\n") for line in rawData]

    # Convert to ints
    # data = list(map(int, rawData))

    print(f"Part 1: {}")
    #print(f"Part 2: {}")

    return 0


if __name__ == "__main__":
    #raise SystemExit(main("input_ff/day01.txt"))
    raise SystemExit(main('input_sri/day01.txt'))


# Tests
test_data = []


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
def test_f(input_data: list[int], expected: int) -> None:
    assert f(input_data) == expected


# Part 2 test
#@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
#def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
