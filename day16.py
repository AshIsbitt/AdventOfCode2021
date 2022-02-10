# Part 1: Decode the structure of your hexadecimal-encoded BITS transmission;
# what do you get if you add up the version numbers in all packets?
from __future__ import annotations

import pprint as p
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass
from typing import Union

import pyperclip as pyp  # type: ignore
import pytest


TRANSLATION_TABLE = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


@dataclass
class Packet:
    version: int
    type_id: int
    sub_packets: Union[list[Packet], list[str]]
    mode: int = -1


def hex_to_bin(msg: str) -> str:
    new_msg = ""
    for char in msg.strip():
        new_msg += TRANSLATION_TABLE[char]

    return new_msg


def bin_to_den(msg: str) -> int:
    return int(msg, 2)


def get_header(msg: str, ptr: int) -> tuple[int, int]:
    version = bin_to_den(f"0{msg[ptr:ptr+3]}")
    type_id = bin_to_den(f"0{msg[ptr+3:ptr+6]}")
    return (version, type_id)


def get_literal_nibble(msg: str, ptr: int) -> str:
    return msg[ptr : ptr + 5]


def parse_packet(bin_str: str, ptr: int) -> list[Packet]:
    version, type_id = get_header(bin_str, ptr)
    ptr += 6

    if type_id == 4:
        # calculate literal
        packets = []

        while True:
            nibble = get_literal_nibble(bin_str, ptr)
            ptr += 5
            packets.append(nibble[1:])

            if not int(nibble[0]):
                break

        return [Packet(version=version, type_id=type_id, sub_packets=packets)]

    else:
        # get operator
        mode = int(bin_str[ptr])
        ptr += 1

        if mode:
            ...
        else:
            ...

        pass

    return []


# Part 1
def packet_decoder(msg: str, version_total: int = 0) -> int:
    version_total = 0

    binary_string = hex_to_bin(msg)
    packets = parse_packet(binary_string, 0)

    for packet in packets:
        version_total += packet.version

    #     if not type_id == 4:
    #         length_type_id = get_length_id(binary_string)
    #         binary_string = binary_string[1:]
    #
    #         # check length data
    #         if length_type_id:
    #             packet_count = int(binary_string[:12])
    #             binary_string = binary_string[12:]
    #
    #             # remove trailing zeros
    #             while binary_string[-1] == "0":
    #                 binary_string = binary_string[:-1]
    #
    #             # split string into equal length packets
    #             packets = [
    #                 binary_string[start : start + packet_count]
    #                 for start in range(0, len(binary_string), packet_count)
    #             ]
    #
    #             for packet in packets:
    #                 version_total += packet_decoder(packet, version_total)
    #
    #         else:
    #             bit_length = int(binary_string[:15])
    #             binary_string = binary_string[15:]
    #
    #             while len(binary_string) >= bit_length:
    #                 version_total += packet_decoder(
    #                     binary_string[0:bit_length], version_total
    #                 )
    #                 binary_string = binary_string[bit_length:]

    return version_total


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
    assert packet_decoder(input_data, 0) == expected


bin_test_data_2 = "00111000000000000110111101000101001010010001001000000000"


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("D2FE28", "110100101111111000101000"),
        ("38006F45291200", bin_test_data_2),
    ],
)
def test_hex_to_bin(input_data, expected):
    assert hex_to_bin(input_data) == expected


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
