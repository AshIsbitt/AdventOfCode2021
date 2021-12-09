# To guarantee victory against the giant squid, figure out which board will win
# first. What will your final score be if you choose that board?
import pprint as p
from collections import Counter
from dataclasses import dataclass

import pytest


@dataclass
class Board:
    layout: list[list[dict[int, bool]]]

    def __init__(self, boardlayout):
        self.layout = []
        emptyList: list[tuple[int, bool]] = []

        for item in boardlayout:
            emptyList.append({int(item): False})

            if len(emptyList) == 5:
                self.layout.append(emptyList)
                emptyList = []

    def score(self, finalNum: int) -> int:
        score = 0

        for x in self.layout:
            for y in self.layout[x]:
                if not self.layout[x][y][1]:
                    score += self.layout[x][y][0]

        return score * finalNum

    def hasWon(self) -> bool:
        pass
        # Check rows
        for e, x in enumerate(self.layout):
            for en, y in enumerate(self.layout[x]):
                if not self.layout[e][en][1]:
                    break
            else:
                return True

            # Check columns
            # for en, y in enumerate(self.layout[x]):

    def mark(self, num: int) -> None:
        for e, x in enumerate(self.layout):
            for en, y in enumerate(self.layout[e]):
                self.layout[e][en][num] = True


def bingoSubsystem(rawData: str) -> int:
    finalScore = 0

    numbers, *boards = rawData.split("\n\n")

    numberList = [int(i) for i in numbers.split(",")]
    boardObjects = [Board(board.split()) for board in boards]

    for num in numberList:
        for board in boardObjects:
            board.mark(num)
            print(f"{num} Marked")

            if board.hasWon():
                finalScore = board.score(num)

    return finalScore


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    winningScore = bingoSubsystem(rawData)
    print(f"Part 1: {winningScore}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day04.txt"))
    # raise SystemExit(main('input_sri/day04.txt'))


# Tests
test_data = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


# Part 1 test
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 4512),))
def test_bingoSubsystem(input_data: str, expected: int) -> None:
    assert bingoSubsystem(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
