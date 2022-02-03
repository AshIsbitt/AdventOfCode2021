# Part 1: Decode the structure of your hexadecimal-encoded BITS transmission;
# what do you get if you add up the version numbers in all packets?
import pprint as p
from collections import Counter
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


# Part 1
def packet_decoder(data: str) -> int:
    pass


def main(filename: str) -> int:
    with open(filename) as input_data:
        raw_data = input_data.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = packet_decoder(raw_data)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day16.txt"))
    raise SystemExit(main("input_sri/day16.txt"))


# Tests
# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_packet_decoder(input_data, expected):
    assert packet_decoder(input_data) == expected


# Part 2 test
"""
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ]
)
def test_f(input_data, expected):
    assert f(input_data) == expected
"""
