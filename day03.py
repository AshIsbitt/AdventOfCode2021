# Part 1: Use the binary numbers in your diagnostic report to calculate the
# gamma rate and epsilon rate, then multiply them together. What is the power
# consumption of the submarine?
# Part 2: Use the binary numbers in your diagnostic report to calculate the
# oxygen generator rating and CO2 scrubber rating, then multiply them together.
# What is the life support rating of the submarine?
import pytest


def lifeSupportRating(rawData: list[str]) -> int:
    o2Rate: int = 0
    co2ScrubRate: int = 0

    return o2Rate * co2ScrubRate


def getGammaEpsilonCount(rawData: list[str]) -> int:
    gamma: str = ""
    epsilon: str = ""

    counter = [0] * (len(rawData[0]))

    for item in rawData:
        charItem = list(item)

        for i, char in enumerate(charItem):
            if char == "1":
                counter[i] += 1
                print(counter)

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

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day03.txt"))
    # raise SystemExit(main("input_sri/day03.txt"))


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


@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 230),))
def test_lifeSupportRating(input_data: list[str], expected: int) -> None:
    assert lifeSupportRating(input_data) == expected
