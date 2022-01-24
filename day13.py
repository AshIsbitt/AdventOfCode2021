# Part 1: How many dots are visible after completing just the first fold
# instruction on your transparent paper?
import pyperclip as pyp  # type: ignore
import pytest


def parse_input(rawData: str) -> tuple[list[tuple[int, int]], list[tuple[str, int]]]:
    fold_list: list[tuple[str, int]] = []
    points_list: list[tuple[int, int]] = []

    points, folds = rawData.split("\n\n")

    for line in folds.splitlines():
        fa = line[11:]
        a, b = fa.split("=")
        fold_list.append((a, int(b)))

    for line in points.splitlines():
        a, b = line.split(",")
        points_list.append((int(a), int(b)))

    return (points_list, fold_list)


# Part 1
def first_fold(rawData: str) -> int:
    points, folds = parse_input(rawData)
    print(points)
    print(folds)

    return 0


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = first_fold(rawData)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day13.txt"))
    raise SystemExit(main("input_sri/day13.txt"))


# Tests
test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 17),
    ],
)
def test_first_fold(input_data, expected) -> None:
    assert first_fold(input_data) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data, expected) -> None:
    assert f(input_data) == expected
"""
