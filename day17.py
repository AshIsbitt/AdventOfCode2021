# Part 1: Find the initial velocity that causes the probe to reach the highest
# y position and still eventually be within the target area after any step.
# What is the highest y position it reaches on this trajectory?
import pprint as p
from collections import Counter
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(inp: str) -> dict[str, int]:
    x, y = (inp.split(": "))[1].split(", ")
    x_s, x_e = x.split("..")
    y_s, y_e = y.split("..")

    data: dict[str, int] = {}
    data["x_start"] = int(x_s[2:])
    data["x_end"] = int(x_e)
    data["y_start"] = int(y_s[2:])
    data["y_end"] = int(y_e)
    return data


def check_trajectory(x: int, y: int, targets: dict[str, int]) -> int:

    x_pos = 0
    y_pos = 0
    highest_point = 0
    success = False

    while True:
        x_pos += x
        y_pos += y

        if x > 0:
            x -= 1
        elif x < 0:
            x += 1

        y -= 1

        if y_pos < highest_point:
            highest_point = y_pos

        if x_pos in range(targets["x_start"], targets["x_end"]) and y_pos in range(
            targets["y_start"], targets["y_end"]
        ):

            success = True
            break
        elif x_pos > targets["x_end"] or y_pos > targets["y_end"]:
            break

    if success:
        return highest_point
    else:
        return 0


def get_highest_value(valid: dict[tuple[int, int], int]) -> tuple[int, int]:
    return max(valid, key=lambda key: valid[key])


def trajectory_iterator(targets: dict[str, int]) -> int:
    valid: dict[tuple[int, int], int] = {}

    RANGE_CHECK = 2500
    for x in range(1, RANGE_CHECK):
        for y in range(-RANGE_CHECK, RANGE_CHECK):
            # returns an int with it's highest y value or 0 if it's not within target area
            highest_point = check_trajectory(x, y, targets)

            if highest_point != 0:
                valid[(x, y)] = highest_point

    highest_val = valid[get_highest_value(valid)]
    return highest_val


# Part 1
def calc_trajectory(data: str) -> int:
    targets = parse_input(data)
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


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ({"a": 4, "b": 6, "c": 12, "d": 5}, "c"),
    ],
)
def test_get_highest_value(input_data, expected):
    assert get_highest_value(input_data) == expected


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
