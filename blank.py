# What to do
import pytest
import pyperclip as pyp # type: ignore


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()
    rawData = [line.rstrip("\n") for line in rawData]

    # Convert to ints
    # data = list(map(int, rawData))

    if 'sri' in filename:
        print('Browser: Safari')
    elif 'ff' in filename:
        print('Browser: Firefox')

    p1 = pass
    print(f"Part 1: {p1}")
    #p2 = pass
    #print(f"Part 2: {p2}")

    try:
        pyp.copy(p2)
        print('Copied: Part 2')
    except NameError:
        pyp.copy(p1)
        print('Copied: Part 1')

    return 0


if __name__ == "__main__":
    #raise SystemExit(main("input_ff/day01.txt"))
    raise SystemExit(main('input_sri/day01.txt'))


# Tests
test_data = []


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data: list[int], expected: int) -> None:
    assert f(input_data) == expected


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
