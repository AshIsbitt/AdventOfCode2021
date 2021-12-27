# Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?
import pytest


def parse_records(rawData: list[str]) -> list[list[str]]:
    parsed_data = []

    for record in rawData:
        r = record.strip()
        parsed_data.append(r.split(" | "))

    return parsed_data


def identify_unique_segments(rawData: list[str]) -> int:
    unique_segments = 0
    parsed_data = parse_records(rawData)

    return unique_segments


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    print(f"Part 1: {identify_unique_segments(rawData)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day08.txt"))
    # raise SystemExit(main('input_sri/day08.txt'))


# Tests
test_data_1 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
test_data_2 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


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
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[str], expected: int) -> None:
#    assert f(input_data) == expected
