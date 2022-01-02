# Part 1: Find the first illegal character in each corrupted line of the
# navigation subsystem. What is the total syntax error score for those errors?
from collections import Counter

import pytest


def char_points(char: str) -> int:
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    return points[char]


def locate_corrupted_lines(rawData: list[str]) -> int:
    total_score = 0
    token_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    buffer = []

    for line in rawData:
        for token in line:
            if token in token_pairs.keys():
                buffer.append(token)

            elif token in token_pairs.values():
                token_key = [k for k, v in token_pairs.items() if v == token][0]

                if buffer[-1] == token_key:
                    buffer.pop(-1)
                else:
                    total_score += char_points(token)
                    break

        if len(buffer):
            # Line is incomplete
            buffer = []

    return total_score


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()
    rawData = [line.rstrip("\n") for line in rawData]

    print(f"Part 1: {locate_corrupted_lines(rawData)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day10.txt"))
    # raise SystemExit(main('input_sri/day10.txt'))


# Tests
test_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 26397),
    ],
)
def test_locate_corrupted_lines(input_data: list[str], expected: int) -> None:
    assert locate_corrupted_lines(input_data) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
 def test_f(input_data: list[int], expected: int) -> None:
   assert f(input_data) == expected
"""
