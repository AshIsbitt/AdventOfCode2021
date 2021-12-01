# How many measurements are larger than the previous measurement?
import pytest


def depthIncreaseDetector(depthData: list[int]) -> int:
    counter: int = 0

    for itera, item in enumerate(depthData):
        if depthData[itera] > depthData[itera - 1]:
            counter += 1

    return counter


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    depthData = list(map(int, rawData))

    depthCounter = depthIncreaseDetector(depthData)
    print(f"Part 1: {depthCounter}")
    return 0


if __name__ == "__main__":
    # raise SystemExit(main('input_ff/day01.txt'))
    raise SystemExit(main("input_sri/day01.txt"))


# Tests

test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 7),))
def test_depthIncreaseDetector(input_data: list[int], expected: int) -> None:
    assert depthIncreaseDetector(input_data) == expected
