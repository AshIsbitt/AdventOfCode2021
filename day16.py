# Part 1: Decode the structure of your hexadecimal-encoded BITS transmission;
# what do you get if you add up the version numbers in all packets?
# Part 2: What do you get if you evaluate the expression represented by your
# hexadecimal-encoded BITS transmission?
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
    mode: int
    sub_packets: Union[list[Packet], list[str]]


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


def parse_packet(ptr: int, bin_str: str) -> tuple[int, Packet]:
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

        return ptr, Packet(version, type_id, -1, packets)

    else:
        # get operator
        mode = int(bin_str[ptr])
        ptr += 1

        if mode:
            packet_count = bin_to_den(bin_str[ptr : ptr + 11])
            ptr += 11

            packet_list: list[Packet] = []

            for _ in range(packet_count):
                ptr, packet = parse_packet(ptr, bin_str)
                packet_list.append(packet)

            return ptr, Packet(version, type_id, mode, packet_list)

        else:
            packet_length = bin_to_den(bin_str[ptr : ptr + 15])
            ptr += 15

            new_ptr = ptr
            ptr += packet_length

            packet_list = []

            while new_ptr < ptr:
                new_ptr, packet = parse_packet(new_ptr, bin_str)
                packet_list.append(packet)

            return ptr, Packet(version, type_id, mode, packet_list)


def get_version_total(packet_stack: Packet) -> int:
    version_total = 0
    packet_heap: list[Packet] = [packet_stack]

    while packet_heap:
        pkt = packet_heap.pop()
        version_total += pkt.version

        if pkt.mode != -1:
            packet_heap.extend(pkt.sub_packets)  # type: ignore

    return version_total


# Part 1
def packet_decoder(msg: str, version_total: int = 0) -> int:
    binary_string = hex_to_bin(msg)
    _, packet_stack = parse_packet(0, binary_string)

    return get_version_total(packet_stack)


def eval_packet(pkt) -> int:
    if pkt.type_id == 0:
        return sum(eval_packet(sub_pkt) for sub_pkt in pkt.sub_packets)
    elif pkt.type_id == 1:
        val = 1
        for sub_pkt in pkt.sub_packets:
            val *= eval_packet(sub_pkt)
        # val *= [eval_packet(sub_pkt) for sub_pkt in pkt.sub_packets]
        return val
    elif pkt.type_id == 2:
        return min(eval_packet(sub_pkt) for sub_pkt in pkt.sub_packets)
    elif pkt.type_id == 3:
        return max(eval_packet(sub_pkt) for sub_pkt in pkt.sub_packets)
    elif pkt.type_id == 4:
        return bin_to_den("".join(pkt.sub_packets))
    elif pkt.type_id == 5:
        return eval_packet(pkt.sub_packets[0]) > eval_packet(pkt.sub_packets[1])
    elif pkt.type_id == 6:
        return eval_packet(pkt.sub_packets[0]) < eval_packet(pkt.sub_packets[1])
    elif pkt.type_id == 7:
        return eval_packet(pkt.sub_packets[0]) == eval_packet(pkt.sub_packets[1])
    else:
        raise AssertionError


# Part 2
def calculate_packet_values(msg: str) -> int:
    binary_string = hex_to_bin(msg)
    _, packet_stack = parse_packet(0, binary_string)

    return eval_packet(packet_stack)


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

    p2 = calculate_packet_values(raw_data)
    pyp.copy(p2)
    print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day16.txt"))
    # raise SystemExit(main("input_sri/day16.txt"))


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


# Part 2 tests
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_calculate_packet_values(input_data, expected):
    assert calculate_packet_values(input_data) == expected
