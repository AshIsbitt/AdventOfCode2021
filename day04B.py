# Part 1: To guarantee victory against the giant squid, figure out which board
# will win first. What will your final score be if you choose that board?
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

        for row in self.layout:
            for val in row:
                if not next(iter(val.values())):
                    score += next(iter(val.keys()))

        return score * finalNum

    def hasWon(self, num) -> bool:
        # Check rows
        for x in range(5):
            if all([next(iter(d.values())) for d in self.layout[x]]):
                return True
            elif all(all(self.layout[y][x].values()) for y in range(5)):
                return True

        return False

    def mark(self, num: int) -> None:
        for row in self.layout:
            for value in row:
                value.update((num, True) for k, v in value.items() if k == num)


def bingoParser(rawData: str) -> tuple[list[int], list[Board]]:

    numbers, *boards = rawData.split("\n\n")
    numberList = [int(i) for i in numbers.split(",")]
    boardObjects = [Board(board.split()) for board in boards]

    return numberList, boardObjects


def bingoSubsystem(rawData: str) -> int:
    finalScore = 0
    numberList, boardObjects = bingoParser(rawData)

    for num in numberList:
        for board in boardObjects:
            board.mark(num)

            if board.hasWon(num):
                finalScore = board.score(num)
                return finalScore

    return finalScore


def finalWinner(rawData):
    finalScore = 0
    numberList, boardObjects = bingoParser(rawData)

    return finalScore


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    winningScore = bingoSubsystem(rawData)
    print(f"Part 1: {winningScore}")

    lastWinningScore = finalWinner(rawData)
    print(f"Part 2: {lastWinningScore}")

    return 0


if __name__ == "__main__":
    # raise SystemExit(main("input_ff/day04.txt"))
    raise SystemExit(main("input_sri/day04.txt"))


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
@pytest.mark.parametrize(("input_data", "expected"), ((test_data, 1924),))
def test_finalWinner(input_data: list[int], expected: int) -> None:
    assert finalWinner(input_data) == expected
