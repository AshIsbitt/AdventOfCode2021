# Part 1: Find the initial velocity that causes the probe to reach the highest
# y position and still eventually be within the target area after any step.
# What is the highest y position it reaches on this trajectory?
# Part 2: How many distinct initial velocity values cause the probe to be
# within the target area after any step?
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


def trajectory_iterator(targets: dict[str, int], p2: bool = False) -> int:
    highest_peak = 0
    print(targets)

    for x in range(500):
        for y in range(500):
            x_pos = 0
            y_pos = 0
            x_vel = x
            y_vel = y
            max_height = 0
            complete = False

            for _ in range(330):
                x_pos += x_vel
                y_pos += y_vel
                max_height = max(max_height, y_pos)

                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1

                y_vel -= 1

                if (
                    targets["x_start"] <= x_pos <= targets["x_end"]
                    and targets["y_start"] <= y_pos <= targets["y_end"]
                ):

                    complete = True

            if complete:
                highest_peak = max(max_height, highest_peak)

    return highest_peak


# Part 1
def calc_trajectory(data: str) -> int:
    targets = parse_input(data)
    highest_val = trajectory_iterator(targets)
    return highest_val


# Part 2
def get_all_successful_trick_shots(data: str) -> int:
    targets = parse_input(data)
    trick_shot_count = trajectory_iterator(targets, True)
    return trick_shot_count


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

    p2 = get_all_successful_trick_shots(raw_data)
    pyp.copy(p2)
    print(f"Part 2: {p2}")

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
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("target area: x=20..30, y=-10..-5", 112),
    ],
)
def test_f(input_data, expected):
    assert get_all_successful_trick_shots(input_data) == expected
