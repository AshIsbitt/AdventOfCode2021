# Part 1: What do you get if you take the quantity of the most common element
# and subtract the quantity of the least common element?
import copy
import pprint as p
from collections import Counter

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(rawData: str) -> tuple[str, dict[str, str]]:
    lines = rawData.splitlines()
    polymer = lines[0].strip()
    data = {}

    for item in lines[2:]:
        vals = item.split(" -> ")
        data[vals[0]] = vals[1]

    return polymer, data


def get_score(poly: dict[str, int], final_char: str) -> int:
    char_count: dict[str, int] = Counter()

    for i in poly.keys():
        char_count[i[0]] += poly[i]

    char_count[final_char] += 1

    return max(char_count.values()) - min(char_count.values())


def get_new(substr: str, data: dict[str, str]) -> tuple[str, str]:
    new_char = data[substr]
    a = substr[0] + new_char
    b = new_char + substr[1]

    return a, b


def poly_growth(polymer: str, data: dict[str, str], steps: int) -> dict[str, int]:
    # {pair of chars : count of that pair}
    patterns: Counter[str] = Counter()

    # propogate patterns with first iteration
    for idx, letter in enumerate(polymer[1:]):
        substr = polymer[idx] + letter
        new_substr = get_new(substr, data)

        patterns[new_substr[0]] += 1
        patterns[new_substr[1]] += 1

    # continually get more pairs
    for _ in range(steps):
        iter_pairs: Counter[str] = Counter()

        for pair, count in patterns.items():
            new_substr = get_new(pair, data)

            iter_pairs[new_substr[0]] += count
            iter_pairs[new_substr[1]] += count

        patterns = iter_pairs
        print(iter_pairs)

    return patterns


# Part 1
# Part 2
def form_polymers(rawData: str, steps: int) -> int:
    polymer, data = parse_input(rawData)
    poly = poly_growth(polymer, data, steps)

    score = get_score(poly, polymer[-1])
    return score


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = form_polymers(rawData, 10)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day14.txt"))
    raise SystemExit(main("input_sri/day14.txt"))


# Tests
test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "steps", "expected"),
    [
        (test_data, 10, 1588),
    ],
)
def test_form_polymers(input_data, steps, expected):
    assert form_polymers(input_data, steps) == expected


# NNCB
# NCNBCHB
# NBCCNBBBCBHCB
# NBBBCNCCNBBNBNBBCHBHHBCHB
# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
