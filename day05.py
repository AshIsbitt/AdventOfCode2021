# Part 1: Consider only horizontal and vertical lines. At how many points do
# at least two lines overlap?
import pytest


class Coordinate:
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, line: str):
        chunks = line.split(" -> ")

        chunk1 = chunks[0].split(",")
        self.x1 = int(chunk1[0])
        self.y1 = int(chunk1[1])

        chunk2 = chunks[1].split(",")
        self.x2 = int(chunk2[0])
        self.y2 = int(chunk2[1])


def ventMapping(rawData: list[str]) -> int:
    safe_routes = 0

    coordinates = []

    for line in rawData:
        coordinates.append(Coordinate(line))

    return safe_routes


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    countOfDangers = ventMapping(rawData)
    print(f"Part 1: {countOfDangers}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day05.txt"))
    # raise SystemExit(main('input_sri/day05.txt'))


# Tests
test_data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 5),))
def test_ventMapping(input_data: list[str], expected: int) -> None:
    assert ventMapping(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
