# Part 1: Find the first illegal character in each corrupted line of the
# navigation subsystem. What is the total syntax error score for those errors?
import pytest


def illegal_char_scorer(rawData: list[str]) -> int:
    total_score = 0

    return total_score


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()
    rawData = [line.rstrip("\n") for line in rawData]

    print(f"Part 1: {illegal_char_scorer(rawData)}")
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
def test_illegal_char_scorer(input_data: list[str], expected: int) -> None:
    assert illegal_char_scorer(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
