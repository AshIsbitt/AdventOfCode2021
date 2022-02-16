# Part 1: Find the initial velocity that causes the probe to reach the highest
# y position and still eventually be within the target area after any step.
# What is the highest y position it reaches on this trajectory?
import pprint as p
from collections import Counter
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(data: str) -> tuple[tuple[int, int], tuple[int, int]]:
    x, y = (data.split(": "))[1].split(", ")
    x_s, x_e = x.split("..")
    y_s, y_e = y.split("..")
    return ((int(x_s[2:]), int(x_e)), (int(y_s[2:]), int(y_e)))


def check_trajectory(
    x: int, y: int, targets: tuple[tuple[int, int], tuple[int, int]]
) -> int:

    x_pos = x
    y_pos = y
    highest_point = 0
    success = False

    while True:
        x_pos += x
        y_pos += y

        if x_pos > 0:
            x_pos -= 1
        elif x_pos < 0:
            x_pos += 1

        y_pos -= 1

        print(x_pos, y_pos)
        if y_pos < highest_point:
            highest_point = y_pos

        if x_pos in range(*targets[0]) and y_pos in range(*targets[1]):
            success = True
            break
        elif x_pos > targets[0][1] or y_pos > targets[1][1]:
            break

    if success:
        return highest_point
    else:
        return 0


def get_highest_value(valid: dict[tuple[int, int], int]) -> tuple[int, int]:
    return max(valid, key=lambda key: valid[key])


def trajectory_iterator(targets: tuple[tuple[int, int], tuple[int, int]]) -> int:
    valid: dict[tuple[int, int], int] = {}

    RANGE_CHECK = 25
    for x in range(1, RANGE_CHECK):
        for y in range(1, RANGE_CHECK):
            # returns an int with it's highest y value or 0 if it's not within target area
            highest_point = check_trajectory(x, y, targets)

            print(highest_point)
            if highest_point != 0:
                valid[(x, y)] = highest_point

    highest_val = valid[get_highest_value(valid)]
    return highest_val


# Part 1
def calc_trajectory(data: str) -> int:
    targets = parse_input(data)
    # generate each iterator up to(10,10) starting at (1,1)
    highest_val = trajectory_iterator(targets)
    return highest_val


def main(filename: str) -> int:
    with open(filename) as input_data:
        raw_data = input_data.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = calc_trajectory(raw_data)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day17.txt"))
    raise SystemExit(main("input_sri/day17.txt"))


# Tests
# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("target area: x=20..30, y=-10..-5", 45),
    ],
)
def test_calc_trajectory(input_data, expected):
    assert calc_trajectory(input_data) == expected


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
