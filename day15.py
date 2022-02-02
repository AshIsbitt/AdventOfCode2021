# Part 1: What is the lowest total risk of any path from the top left to the
# bottom right?
import heapq
import pprint as p
from collections import Counter
from collections import defaultdict
from typing import Generator

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(raw_data: str) -> tuple[dict[tuple[int, int], int], int]:
    line_len = len(raw_data.splitlines()[0])
    data = {}

    for idx, line in enumerate(raw_data.splitlines()):
        for idy, char in enumerate(line):
            data[(idx, idy)] = int(char)

    return data, line_len


def neighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield (x + 1, y)
    yield (x - 1, y)
    yield (x, y + 1)
    yield (x, y - 1)


def dijkstra(graph, src: tuple[int, int], dest: tuple[int, int]) -> int:
    # Graph = (x, y): risk

    # Adding to what's been seen, not tracking what's yet to be visited
    visited_set: set[tuple[int, int]] = set()

    # priority queue: (risk, (x, y))
    cell_queue = [(0, (0, 0))]

    while cell_queue:
        # get first value in priority queue
        current_risk, current_cords = heapq.heappop(cell_queue)

        if current_cords in visited_set:
            continue
        elif current_cords == dest:
            break
        else:
            visited_set.add(current_cords)

        x, y = current_cords
        for adj in neighbors(x, y):
            if adj in graph:
                heapq.heappush(cell_queue, (current_risk + graph[adj], adj))

    return current_risk


# Part 1
def shortest_route(raw_data: str) -> int:
    data, line_len = parse_input(raw_data)
    shortest_risk_lvl = dijkstra(data, (0, 0), (line_len, line_len))
    return shortest_risk_lvl


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
