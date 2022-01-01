# Part 1: Find the first illegal character in each corrupted line of the
# navigation subsystem. What is the total syntax error score for those errors?
import pytest


def char_points(char: str) -> int:
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    return points[char]


def locate_corrupted_chars(rawData: list[str]) -> int:
    total_score = 0

    return total_score


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()
    rawData = [line.rstrip("\n") for line in rawData]

    print(f"Part 1: {locate_corrupted_chars(rawData)}")
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
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 26397),))
def test_locate_corrupted_chars(input_data: list[str], expected: int) -> None:
    assert locate_corrupted_chars(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
