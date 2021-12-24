# Part 1: Consider only horizontal and vertical lines. At how many points do
# at least two lines overlap?
# Part 2: Unfortunately, considering only horizontal and vertical lines doesn't
# give you the full picture; you need to also consider diagonal lines.
import pprint as p
from collections import Counter

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


def ventMapping(rawData: list[str], get_diagonals: bool = False) -> int:
    safe_routes = 0
    coordinates = []

    for line in rawData:
        coordinates.append(Coordinate(line))

    map_cords: Counter[tuple[int, int]] = Counter()

    for point in coordinates:

        if point.x1 == point.x2:
            for i in range(min(point.y1, point.y2), max(point.y1, point.y2) + 1):
                map_cords[(point.x1, i)] += 1
        elif point.y1 == point.y2:
            for j in range(min(point.x1, point.x2), max(point.x1, point.x2) + 1):
                map_cords[(j, point.y1)] += 1
        # Part 2
        elif get_diagonals:
            # print(point.x1, point.y1, point.x2, point.y2)
            if abs(point.x1 - point.x2) == abs(point.y1 - point.y2):
                start_point = min((point.x1, point.y1), (point.x2, point.y2))
                end_point = max((point.x1, point.y1), (point.x2, point.y2))

                marker = list(start_point)
                while tuple(marker) <= end_point:
                    x, y = marker  # Destructuring marker so mypy doesn't cry
                    map_cords[x, y] += 1

                    if marker[0] <= end_point[0]:
                        marker[0] += 1
                    elif marker[0] >= end_point[0]:
                        marker[0] -= 1

                    if marker[1] <= end_point[1]:
                        marker[1] += 1
                    elif marker[1] >= end_point[1]:
                        marker[1] -= 1

    safe_routes = len([i for i in map_cords.values() if i >= 2])

    return safe_routes


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    countOfDangers = ventMapping(rawData)
    print(f"Part 1: {countOfDangers}")

    dangers_on_diagonals = ventMapping(rawData, True)
    print(f"Part 2: {dangers_on_diagonals}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day05.txt"))
    # raise SystemExit(main("input_sri/day05.txt"))


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
@pytest.mark.parametrize(
    ("input_data", "boolean", "expected"),
    (
        (test_data, False, 5),
        (test_data, True, 12),
    ),
)
def test_ventMapping(input_data: list[str], boolean: bool, expected: int) -> None:
    assert ventMapping(input_data, boolean) == expected
