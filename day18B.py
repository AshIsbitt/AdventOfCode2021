# Part 1: Add up all of the snailfish numbers from the homework assignment in
# the order they appear. What is the magnitude of the final sum?
# Part 2: What is the largest magnitude of any sum of two different snailfish
# numbers from the homework assignment?
# Inspired by: https://github.com/alexander-yu/adventofcode/blob/master/problems_2021/18.py
import ast
import itertools
from typing import Any
from typing import Optional
from typing import Union

import pyperclip as pyp
import pytest


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


# Part 2
def find_two_nums(data: list[object]) -> int:
    tree: list[Node] = []
    for item in data:
        tree.append(build_tree(item))

    print([i.value for i in tree])
    all_pairs = [
        n1.value + n2.value
        if n1.value and n2.value is not None
        else Node(None, None, 0)
        for n1, n2 in itertools.permutations(tree, 2)
    ]

    # print(i.value for i in all_pairs)
    ret = max(all_pairs, key=lambda x: x.value)
    return ret.value


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

    p2 = find_two_nums(raw_data)
    pyp.copy(p2)
    print(f"Part 2: {p2}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day18.txt"))
    raise SystemExit(main("input_sri/day18.txt"))


test_data = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 4140),
    ],
)
def test_calculate_homework(input_data: str, expected: int) -> None:
    lst = [ast.literal_eval(itm) for itm in input_data.splitlines()]
    assert calculate_homework(lst) == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (test_data, 3993),
    ],
)
def test_find_two_nums(input_data: str, expected: int) -> None:
    lst = [ast.literal_eval(itm) for itm in input_data.splitlines()]
    assert find_two_nums(lst) == expected
