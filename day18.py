# Part 1:Add up all of the snailfish numbers from the homework assignment in
# the order they appear. What is the magnitude of the final sum?
import ast
import pprint as p
from collections import Counter
from collections import defaultdict
from typing import Union

import pyperclip as pyp  # type: ignore
import pytest


def get_magnitude(base: object):
    """3x the left element plus 2x the right element"""
    if isinstance(base, list):
        return (3 * get_magnitude(base[0])) + (2 * get_magnitude(base[1]))
    else:
        return base


def split(base: object) -> tuple[bool, object]:
    """Turn a single number greater than 9 into 2-len list"""
    if isinstance(base, list):
        return False, split(base[0])
    elif isinstance(base, int):
        if base > 9:
            return False, [base // 2, (base + 1) // 2]
        else:
            return True, base

    return True, base


def explode(base: object) -> tuple[bool, object]:
    """Add a 2-len list's values to outer values and replace with 0"""
    return False, 0


def add_numbers(n1: object, n2: object) -> object:
    """Turn two values into a 2-length list"""
    return [n1, n2]


def number_homework(raw_data: list[object]) -> int:
    start = raw_data[0]
    for item in raw_data[1:]:
        start = add_numbers(start, item)

        exp = True
        while exp:
            exp, start = explode(start)

        spl = True
        while spl:
            spl, start = split(start)

    return get_magnitude(start)


def main(filename: str) -> int:
    raw_data: list[object] = []

    with open(filename) as input_data:
        lines = input_data.readlines()
        for line in lines:
            raw_data.append(ast.literal_eval(line))

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = number_homework(raw_data)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day18.txt"))
    raise SystemExit(main("input_sri/day18.txt"))


# Tests
test_data = [
    [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
    [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
    [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
    [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
    [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
    [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
    [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
    [[9, 3], [[9, 9], [6, [4, 9]]]],
    [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
    [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]],
]


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 4140),
    ],
)
def test_number_homework(input_data, expected):
    assert number_homework(input_data) == expected


test_input_1 = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
]

test_input_2 = [
    [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
    [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
    [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
    [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
    [7, [5, [[3, 8], [1, 4]]]],
    [[2, [2, 2]], [8, [8, 1]]],
    [2, 9],
    [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
    [[[5, [7, 4]], 7], 1],
    [[[[4, 2], 2], 6], [8, 7]],
]

test_output_2 = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_input_1, [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]),
        (test_input_2, test_output_2),
    ],
)
def test_add_numbers(input_data, expected):
    assert add_numbers(input_data) == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (10, [5, 5]),
        (11, [5, 6]),
    ],
)
def test_split(input_data, expected):
    assert split(input_data) == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
        ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
        ),
    ],
)
def test_explode(input_data, expected):
    assert explode(input_data) == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ([[1, 2], [[3, 4], 5]], 143),
        ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
        ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
    ],
)
def test_get_magnitude(input_data, expected):
    assert get_magnitude(input_data) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data, expected):
    assert f(input_data) == expected
"""
