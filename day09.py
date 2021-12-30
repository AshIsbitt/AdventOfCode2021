# Part 1: What is the sum of the risk levels of all low points on your
# heightmap?
import pytest


def parse_input(rawData: list[str]) -> list[list[int]]:
    rawData = [line.rstrip("\n") for line in rawData]

    data_map = []

    for line in rawData:
        row = [int(i) for i in line]
        data_map.append(row)

    return data_map


def risk_mapping(rawData: list[str]) -> int:
    data_map = parse_input(rawData)
    return 0


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    print(f"Part 1: {risk_mapping(rawData)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day1.txt"))
    # raise SystemExit(main('input_sri/day1.txt'))


# Tests
test_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 15),))
def test_risk_mapping(input_data: list[str], expected: int) -> None:
    assert risk_mapping(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
