# Part 1: Find a way to simulate lanternfish. How many lanternfish would there
# be after 80 days?
# Part 2: How many lanternfish would there be after 256 days?
import pytest


def fishBreeder(rawData: list[int], day_length: int) -> int:
    currentGen = {
        0: rawData.count(0),
        1: rawData.count(1),
        2: rawData.count(2),
        3: rawData.count(3),
        4: rawData.count(4),
        5: rawData.count(5),
        6: rawData.count(6),
        7: rawData.count(7),
        8: rawData.count(8),
    }

    for _ in range(day_length):
        # Move each value down 1 in the list
        # 0 -> 6
        # 8 += num of 0s

        zero = currentGen[0]

        for k, v in currentGen.items():
            if k != 0:
                currentGen[k - 1] = v

        currentGen[6] += zero
        currentGen[8] = zero

    return sum(currentGen.values())


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    # Convert to ints
    data = list(map(int, rawData.split(",")))

    fishes = fishBreeder(data, 80)
    print(f"Part 1: {fishes}")

    fishes = fishBreeder(data, 256)
    print(f"Part 2: {fishes}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day06.txt"))
    raise SystemExit(main("input_sri/day06.txt"))


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
