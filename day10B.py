# Part 1: Find the first illegal character in each corrupted line of the
# navigation subsystem. What is the total syntax error score for those errors?
# Part 2: Find the completion string for each incomplete line, score the
# completion strings, and sort the scores. What is the middle score?
import pytest


PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CORRUPTED_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

AUTOCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def locate_mismatch(line: str) -> str | None:
    buffer: list[str] = []

    for token in line:
        if token in PAIRS.keys():
            buffer.append(token)
        elif token in PAIRS.values():
            deleted = buffer.pop()  # delete the last item in the list
            open_pair, *_ = [k for k, v in PAIRS.items() if v == token]

            if deleted != open_pair:
                return token

    return None


def calculate_corruption(rawData: list[str]) -> int:
    scores: list[int] = []

    for line in rawData:
        incorrect_token = locate_mismatch(line)

        if incorrect_token is not None:
            scores.append(CORRUPTED_SCORES[incorrect_token])

    return sum(scores)


def remove_corrupted(rawData: list[str]) -> list[str]:
    pass


def get_missing_chars(line: str) -> str:
    pass


def get_scores(closing_chars: str) -> int:
    pass


def calculate_incomplete(rawData: list[str]) -> int:
    incompletes = remove_corrupted(rawData)
    scores = []

    for line in incompletes:
        missing_chars = get_missing_chars(line)
        scores.append(get_scores(missing_chars))

    ordered_scores = sorted(scores)
    middle_score = ordered_scores[len(ordered_scores) // 2]

    return middle_score


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()
    rawData = [line.rstrip("\n") for line in rawData]

    print(f"Part 1: {calculate_corruption(rawData)}")
    print(f"Part 2: {calculate_incomplete(rawData)}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day10.txt"))
    raise SystemExit(main("input_sri/day10.txt"))


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
def test_calculate_corruption(input_data: list[str], expected: int) -> None:
    assert calculate_corruption(input_data) == expected


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
