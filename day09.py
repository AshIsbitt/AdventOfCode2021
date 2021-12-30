# Part 1: What is the sum of the risk levels of all low points on your
# heightmap?
import pprint as p

import pytest


def parse_input(rawData: list[str]) -> list[list[int]]:
    data = [int(i) for i in rawData if i != "\n"]

    data_map = []

    for item in data:
        transformed_item = str(item)
        row = [int(i) for i in transformed_item]
        data_map.append(row)

    return data_map


def risk_mapping(rawData: list[str]) -> int:
    risk_lvl = 0
    data_map: list[list[int]] = parse_input(rawData)
    print(len(data_map))

    for idx, r in enumerate(data_map):
        for idy, c in enumerate(r):
            # print(idx, idy, c)

            checks = []

            try:
                checks.append(c < data_map[idx][idy + 1])
            except IndexError:
                pass

            try:
                checks.append(c < data_map[idx + 1][idy])
            except IndexError:
                pass

            if idx - 1 >= 0:
                checks.append(c < data_map[idx - 1][idy])

            if idy - 1 >= 0:
                checks.append(c < data_map[idx][idy - 1])

            if all(checks):
                risk_lvl += 1 + c

    return risk_lvl


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    print(f"Part 1: {risk_mapping(rawData)}")
    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day09.txt"))
    raise SystemExit(main("input_sri/day09.txt"))


# Tests
test_data = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 15),))
def test_risk_mapping(input_data: list[str], expected: int) -> None:
    assert risk_mapping(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
