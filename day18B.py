# Part 1: Add up all of the snailfish numbers from the homework assignment in
# the order they appear. What is the magnitude of the final sum?
# Inspired by: https://github.com/alexander-yu/adventofcode/blob/master/problems_2021/18.py
import ast
from typing import Any
from typing import Optional
from typing import Union

import pyperclip as pyp


class Blast:
    def __init__(self, left: Optional["Node"], right: Optional["Node"]) -> None:
        self.left = left
        self.right = right


blast = Blast(None, None)


class Node:
    def __init__(
        self, left: Optional["Node"], right: Optional["Node"], value: Optional[int]
    ) -> None:
        self.left = left
        self.right = right
        self.value = value

    def __add__(self, other: "Node") -> "Node":
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

    def is_empty(self) -> Optional[int]:
        return self.value is None and not self.left and not self.right

    def is_leaf(self) -> bool:
        return not self.left and not self.right

    def add_value(self, value: "Node", side: str) -> None:
        current = self
        while not current.is_leaf():
            current = getattr(current, side)

        if not current.value:
            current.value = 0

        assert value.value is not None
        current.value += value.value

    def absorb_blast(self, blast: Blast, side: str, depth: int) -> Blast:
        if blast == Node(None, None, None):
            return blast

        if depth == 3:
            crater = Node(None, None, 0)
            setattr(self, side, crater)

        other_side = "left" if side == "right" else "right"
        blast_value = getattr(blast, other_side)

        if blast_value:
            getattr(self, other_side).add_value(blast_value, side)

        setattr(blast, other_side, None)
        return blast

    def explode(self, depth: int = 0) -> tuple[bool, Union["Node", Blast]]:
        if self.is_leaf():
            # If a node has no left or right, it's at the bottom
            return False, Node(None, None, None)

        if depth == 4:
            # If a node is 4 deep, it's meant to explode
            assert self.left is not None
            assert self.right is not None

            return True, Node(self.left, self.right, None)

        for side in ["left", "right"]:
            # Check the left and right children of the node
            exploded, blast = getattr(self, side).explode(depth + 1)

            if exploded:
                # Perform the actual maths on the explode operation
                blast = self.absorb_blast(blast, side, depth)
                return True, blast

        return False, Blast(None, None)

    def split_side(self, side: str) -> Union[bool, "Node"]:
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

    def split(self) -> Union["Node", bool]:
        return self.split_side("left") or self.split_side("right")

    def copy(self) -> "Node":
        return Node(
            self.left.copy() if self.left else None,
            self.right.copy() if self.right else None,
            self.value,
        )


def build_tree(num: Any) -> Node:
    if isinstance(num, int):
        return Node(None, None, num)
    else:

        if isinstance(num, Node):
            left = num.left
            right = num.right
        else:
            left, right = num

        return Node(build_tree(left), build_tree(right), None)


def get_magnitude(num: "Node") -> int:

    if num.is_leaf():
        assert isinstance(num.value, int)
        return num.value
    else:
        assert isinstance(num.left, Node)
        assert isinstance(num.right, Node)
        return (3 * get_magnitude(num.left)) + (2 * get_magnitude(num.right))


# Part 1
def calculate_homework(data: list[object]) -> int:
    tree: list[Node] = []
    for item in data:
        tree.append(build_tree(item))

    final_num = sum(tree, start=Node(None, None, None))
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
