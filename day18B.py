# Part 1: Add up all of the snailfish numbers from the homework assignment in
# the order they appear. What is the magnitude of the final sum?
import ast

import pyperclip as pyp
import pytest


class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def is_empty(self):
        return self.value is None and not self.left and not self.right

    def is_leaf(self):
        return not self.left and not self.right

    def __add__(self, other):
        # a.__add__(b) is like doing a + b
        if not isinstance(other, Node):
            raise ValueError(f"Cannot add values of type Node and {type(other)}...")

        if self.is_empty():
            return other.copy()
        else:
            # Create a new parent node with self and other as the children
            result = Node(self.copy(), other.copy(), None)

            while True:
                # reduce instructions
                exploded, _ = result.explode()

                if not exploded:
                    if not result.split():
                        break

            return result

    def explode() -> None:
        ...

    def split_side(self, side: str) -> Node:
        side_node = getattr(self, side)

        if side_node.is_leaf():
            if side_node.value >= 10:
                setattr(
                    self,
                    side,
                    build_tree(
                        [
                            side_node.value // 2,
                            (side_node.value + 1) // 2,
                        ]
                    ),
                )
                return True

            else:
                return False

        else:
            return side_node.split()

    def split(self) -> Node:
        return self.split_side("left") or self.split_side("right")


def build_tree(num: Node | object) -> Node:
    if isinstance(num, int):
        return Node(None, None, num)
    else:
        left, right = num
        return Node(build_tree(left), build_tree(right), None)


def get_magnitude(n):
    ...


# Part 1
def calculate_homework(data: list[object]) -> int:
    tree: list[Node] = []
    for item in data:
        tree.append(build_tree(item))

    final_num = sum(tree, start=Node())
    return get_magnitude(final_num)


def main(filename: str) -> int:
    raw_data: list[object] = []

    with open(filename) as input_data:
        lines = input_data.readlines()
        for line in lines:
            raw_data.append(ast.literal_eval(line))

    if "sri" in filename:
        print("Browser: Safari")
    elif "ff" in filename:
        print("Browser: Firefox")

    p1 = calculate_homework(raw_data)
    pyp.copy(p1)
    print(f"Part 1: {p1}")

    # p2 = 0
    # pyp.copy(p2)
    # print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day18.txt"))
    raise SystemExit(main("input_sri/day18.txt"))


# Tests
test_data = """
"""


# Part 1 test
@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 0),
    ],
)
def test_calculate_homework(input_data, expected):
    assert calculate_homework(input_data) == expected


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
