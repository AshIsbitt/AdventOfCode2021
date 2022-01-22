# Part 1: How many paths through this cave system are there that visit small
# caves at most once?
import pyperclip as pyp  # type: ignore
import pytest


def f():
    pass


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    print(rawData)

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = 0
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day12.txt"))
    raise SystemExit(main("input_sri/day12.txt"))


# Tests
test_data: list[str] = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]

test_data_2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 10),
        (test_data_2, 19),
    ],
)
def test_f(input_data, expected):
    assert f(input_data) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data: list[int], expected: int) -> None:
    assert f(input_data) == expected
"""
