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
        self.is_visited = False


def parse_input(raw_data: str) -> tuple[list[Node], int]:
    data = []
    lines = raw_data.splitlines()
    line_len = len(lines[0])

    for idx, line in enumerate(lines):
        for idy, char in enumerate(line):
            data.append(Node(idx, idy, int(char)))

    return data, line_len


def neighbors(x: int, y: int) -> int:
    yield (x, y + 1)
    yield (x + 1, y)


def dijkstra(graph: list[Node], source: Node, end_point: Node) -> int:
    distance = 0

    for node in graph:
        if node.is_visited:
            continue

        for nearby in neighbors:
            adj, _ = [n for n in graph if n.coords == nearby]

            dist = adj.risk + (node.min_path if node != source else 0)
            if adj.min_path >= dist:
                adj.min_path == dist

        node.is_visited = True

    return 0


# Part 1
def shortest_route(raw_data: str) -> int:
    data, line_len = parse_input(raw_data)

    src, _ = [node for node in data if node.coords == (0, 0)]
    dest, _ = [node for node in data if node.coords == (line_len, line_len)]

    val = dijkstra(data, src, dest)
    print(val)

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
