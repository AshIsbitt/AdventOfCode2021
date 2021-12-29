# Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?
# Part 2: For each entry, determine all of the wire/segment connections and
# decode the four-digit output values. What do you get if you add up all of the
# output values?
import itertools
from collections import defaultdict

import pytest

MAPPING = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6],
}


def parse_records(rawData: list[str]) -> list[list[str]]:
    parsed_data = []

    for record in rawData:
        parsed_data.append(record.split(" | "))

    return parsed_data


def identify_unique_segments(rawData: list[str]) -> int:
    unique_segments = 0
    parsed_data = parse_records(rawData)

    for line in parsed_data:
        output = line[1].split(" ")

        for word in output:
            word = word.strip()
            if len(word) == 3:  # display 7
                unique_segments += 1
            elif len(word) == 4:  # display 4
                unique_segments += 1
            elif len(word) == 2:  # display 1
                unique_segments += 1
            elif len(word) == 7:  # display 8
                unique_segments += 1

    return unique_segments


def validate_perm(perm: tuple[str, ...], line: str) -> bool:
    words = line.split(" ")

    for digit in range(10):
        needed = {perm[idx] for idx in MAPPING[digit]}

        if not any(needed == set(word) for word in words):
            return False

    return True


def calculate_output_vals(rawData: list[str]) -> int:
    parsed_data = parse_records(rawData)
    total_output = 0

    for line in parsed_data:
        for perm in itertools.permutations("abcdefg"):
            is_valid = validate_perm(perm, line[0])

            if is_valid:
                break

        num = "0"

        output = line[1].split(" ")
        for word in output:
            word = word.strip()
            idx = []
            for letter in word:
                idx.append(perm.index(letter))

            idx.sort()

            for k, v in MAPPING.items():
                if v == idx:
                    num += str(k)

        total_output += int(num)
    return total_output


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    print(f"Part 1: {identify_unique_segments(rawData)}")
    print(f"Part 2: {calculate_output_vals(rawData)}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day08.txt"))
    raise SystemExit(main("input_sri/day08.txt"))


# Tests
test_data_1 = [
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
]
test_data_2 = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    (
        (test_data_1, 0),
        (test_data_2, 26),
    ),
)
def test_identify_unique_segments(input_data: list[str], expected: int) -> None:
    assert identify_unique_segments(input_data) == expected


# Part 2 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    (
        (test_data_1, 5353),
        (test_data_2, 61229),
    ),
)
def test_calculate_output_vals(input_data: list[str], expected: int) -> None:
    assert calculate_output_vals(input_data) == expected
