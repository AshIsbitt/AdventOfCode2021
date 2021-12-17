# Part 1: Find a way to simulate lanternfish. How many lanternfish would there
# be after 80 days?
import pytest


def fishBreeder(rawData: list[int], day_length: int) -> int:
    pass


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    # Convert to ints
    data = list(map(int, rawData))

    fishes = fishBreeder(data, 80)
    print(f"Part 1: {fishes}")

    fishes = fishBreeder(data, 256)
    print(f"Part 2: {fishes}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day06.txt"))
    # raise SystemExit(main('input_sri/day06.txt'))


# Tests
test_data = [3, 4, 3, 1, 2]


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "input_length", "expected"),
    (
        (test_data, 18, 26),
        (test_data, 80, 5934),
    ),
)
def test_fishBreeder(input_data: list[int], input_length: int, expected: int) -> None:
    assert fishBreeder(input_data, input_length) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
