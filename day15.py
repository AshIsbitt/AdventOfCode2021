# Part 1: What is the lowest total risk of any path from the top left to the
# bottom right?
import pprint as p
from collections import Counter
from collections import defaultdict

import pyperclip as pyp  # type: ignore
import pytest


class Node:
    def __init__(self, x, y, risk):
        self.coords = (x, y)
        self.risk = risk  # risk value for current node, given by input
        self.min_path = 0  # calculated min path weight from start node to here


def parse_input(raw_data: str) -> list[Node]:
    data = []
    lines = raw_data.splitlines()

    for idx, line in enumerate(lines):
        for idy, char in enumerate(line):
            data.append(Node(idx, idy, int(char)))

    return data


def dijkstra(graph: list[Node], source: Node, end_point: Node) -> None:
    pass


# Part 1
def shortest_route(raw_data: str) -> int:
    data = parse_input(raw_data)
    print(data)
    # val = dijkstra(data)

    return 0


def main(filename: str) -> int:
    with open(filename) as inputData:
        raw_data = inputData.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = shortest_route(raw_data)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day15.txt"))
    raise SystemExit(main("input_sri/day15.txt"))


# Tests
test_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 40),
    ],
)
def test_shortest_route(input_data, expected):
    assert shortest_route(input_data) == expected


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
