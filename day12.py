# Part 1: How many paths through this cave system are there that visit small
# caves at most once?
# Part 2: Given these new rules, how many paths through this cave system are
# there?
from collections import defaultdict
from collections import deque

import pyperclip as pyp  # type: ignore
import pytest


def parse_input(rawData: str) -> dict[str, list[str]]:
    """Create an adjacency list to store the graph"""
    data = defaultdict(list)

    for line in rawData.splitlines():
        src, dest = line.split("-")
        data[src].append(dest)
        data[dest].append(src)

    return data


# Part 2
def path_mapping_plus(rawData: str) -> int:
    edges = parse_input(rawData)

    num_of_routes = 0
    # Where we are, caves we've visited
    start = ("start", set(["start"]), False)
    queue = deque([start])

    while queue:
        pos, caves, is_visited = queue.popleft()

        if pos == "end":
            num_of_routes += 1
            continue

        for node in edges[pos]:
            if node == "start":
                continue
            elif node.islower() and node not in caves:
                new_caves = set(caves)
                new_caves.add(node)

                queue.append((node, new_caves, is_visited))
            elif node.isupper():
                queue.append((node, caves, is_visited))
            elif not is_visited and node in caves:
                queue.append((node, caves, True))

    return num_of_routes


# Part 1
def path_mapping(rawData: str) -> int:
    edges = parse_input(rawData)

    num_of_routes = 0
    # Where we are, caves we've visited
    start = ("start", set(["start"]))
    queue = deque([start])

    while queue:
        pos, caves = queue.popleft()

        if pos == "end":
            num_of_routes += 1
            continue

        for node in edges[pos]:
            if node not in caves:
                new_caves = set(caves)

                if node.islower():
                    new_caves.add(node)

                queue.append((node, new_caves))

    return num_of_routes


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = path_mapping(rawData)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    p2 = path_mapping_plus(rawData)
    pyp.copy(p2)
    print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day12.txt"))
    # raise SystemExit(main("input_sri/day12.txt"))


# Tests
test_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


test_data_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


test_data_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


# Part 1 test
@pytest.mark.parametrize(
    ("args"),
    [
        (test_data, 10),
        (test_data_2, 19),
        (test_data_3, 226),
    ],
)
def test_path_mapping(args):
    assert path_mapping(*args[:-1]) == args[-1]


# Part 2 tests
@pytest.mark.parametrize(
    ("args"),
    [
        (test_data, 36),
        (test_data_2, 103),
        (test_data_3, 3509),
    ],
)
def test_path_mapping_plus(args):
    assert path_mapping_plus(*args[:-1]) == args[-1]
