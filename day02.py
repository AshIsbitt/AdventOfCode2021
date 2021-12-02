# What to do
import pytest


def calcPosition(posData: list[str]) -> int:
    horizontal_pos: int = 0
    vertical_pos: int = 0

    for item in posData:
        moveData = item.split(" ")
        if moveData[0] == "forward":
            horizontal_pos += int(moveData[1])
        elif moveData[0] == "up":
            vertical_pos -= int(moveData[1])
        elif moveData[0] == "down":
            vertical_pos += int(moveData[1])

    return horizontal_pos * vertical_pos


def updatedPosTracker(posData: list[str]) -> int:
    horizontal_pos: int = 0
    vertical_pos: int = 0
    aim: int = 0

    for item in posData:
        moveData = item.split(" ")
        if moveData[0] == "up":
            aim -= int(moveData[1])
        elif moveData[0] == "down":
            aim += int(moveData[1])
        elif moveData[0] == "forward":
            horizontal_pos += int(moveData[1])
            vertical_pos += aim * int(moveData[1])

    return horizontal_pos * vertical_pos


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    # data = list(map(int, rawData))
    current_pos = calcPosition(rawData)
    print(f"Part 1: {current_pos}")

    updatedPos = updatedPosTracker(rawData)
    print(f"Part 2: {updatedPos}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day02.txt"))
    raise SystemExit(main("input_sri/day02.txt"))


# Tests
test_data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 150),))
def test_calcPosition(input_data: list[str], expected: int) -> None:
    assert calcPosition(input_data) == expected


@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 900),))
def test_updatedPosTracker(input_data: list[str], expected: int) -> None:
    assert updatedPosTracker(input_data) == expected
