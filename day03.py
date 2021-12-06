# Part 1: Use the binary numbers in your diagnostic report to calculate the
# gamma rate and epsilon rate, then multiply them together. What is the power
# consumption of the submarine?
# Part 2: Use the binary numbers in your diagnostic report to calculate the
# oxygen generator rating and CO2 scrubber rating, then multiply them together.
# What is the life support rating of the submarine?
import pytest


def binaryCount(rawData: list[str]) -> list[int]:
    counter = [0] * (len(rawData[0]))

    for item in rawData:
        charItem = list(item)

        for i, char in enumerate(charItem):
            if char == "1":
                counter[i] += 1

    return counter


def lifeSupportRating(rawData: list[str], flip: bool = False) -> int:
    gasValue: int = 0

    # List of sets for each bit
    pivotData = list(zip(*rawData))

    for e, val in enumerate(pivotData):
        if len(rawData) <= 2:
            print(flip)
            print(rawData)
            # if flip:
            #    rawData = [i for i in rawData if i[-1] == '0']
            # else:
            #    rawData = [i for i in rawData if i[-1] == '1']

            gasValue = int(rawData[0], 2)
            break

        if not flip:
            # Oxygen
            cb = max(val, key=val.count)
        else:
            # Carbon
            cb = min(val, key=val.count)

        rawData = [item for item in rawData if item[e] == cb]
        pivotData = list(zip(*rawData))

    return gasValue


def getGammaEpsilonCount(rawData: list[str]) -> int:
    gamma: str = ""
    epsilon: str = ""

    counter = binaryCount(rawData)

    for val in counter:
        if val >= (len(rawData) / 2):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)

    return gamma_int * epsilon_int


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    rawData = [line.rstrip("\n") for line in rawData]

    totalRates = getGammaEpsilonCount(rawData)
    print(f"Part 1: {totalRates}")

    oxygen = lifeSupportRating(rawData)
    print(f"{oxygen=}")
    carbon = lifeSupportRating(rawData, True)
    print(f"{carbon=}")
    print(f"Part 2: {oxygen*carbon}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day03.txt"))
    raise SystemExit(main("input_sri/day03.txt"))


# Tests
test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 198),))
def test_getGammaEpsilonCount(input_data: list[str], expected: int) -> None:
    assert getGammaEpsilonCount(input_data) == expected


@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 23),))
def test_lifeSupportRating_oxygen(input_data: list[str], expected: int) -> None:
    assert lifeSupportRating(input_data) == expected


@pytest.mark.parametrize(
    ("input_data", "bool_val", "expected"), ((test_data, True, 10),)
)
def test_lifeSupportRating_carbon(
    input_data: list[str], bool_val: bool, expected: int
) -> None:
    assert lifeSupportRating(input_data, bool_val) == expected
