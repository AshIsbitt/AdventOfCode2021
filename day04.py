# To guarantee victory against the giant squid, figure out which board will win
# first. What will your final score be if you choose that board?
import pprint

import pytest


def parser(rawData: str) -> tuple[list[int], list[list[list[int]]]]:
    drawnNums: list[int] = []
    bingoBoards: list[list[list[int]]] = []

    drawnNums = list(map(int, rawData.split("\n\n", 1)[0].split(",")))
    boardLines = list(map(str, rawData.split("\n\n", 1)[1].split("\n")))
    blankList: list[list[int]] = []
    tempList: list[int] = []

    i = 0

    for item in boardLines:
        if i == 5:
            bingoBoards.append(blankList)
            blankList = []
            i = 0
        else:
            tempList = []
            splitItem = item.split()
            for val in splitItem:
                val = val.lstrip()
                tempList.append(int(val))
            i += 1

            blankList.append(tempList)

    return drawnNums, bingoBoards


def boardScore(nums: list[int], board: list[list[int]]) -> int:
    ret: int = 0

    for row in board:
        for val in row:
            if val not in nums:
                ret += val

    return ret * nums[-1:][0]


def part1(rawData: str) -> int:
    ret: int = 0
    drawnNums, bingoBoards = parser(rawData)

    for e, num in enumerate(drawnNums):
        print(f"{num=}")
        for board in bingoBoards:
            # Rows
            for row in board:
                count = 0
                for item in row:
                    if item in drawnNums[0:e]:
                        count += 1

                if count == 5:
                    ret = boardScore(drawnNums[0:e], board)
                    return ret

            # Columns
            for row in board:
                numID = []
                if num in row:
                    numID.append(row.index(num))

            if len(numID) == 5 and numID.count(numID[0]) == 5:
                ret = boardScore(drawnNums[0:e], board)
                return ret

    return ret


def main(filename: str) -> int:
    with open(filename) as inputData:
        rawData = inputData.read()

    bingoVal = part1(rawData)
    print(f"Part 1: {bingoVal}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("input_ff/day04.txt"))
    # raise SystemExit(main('input_sri/day1.txt'))

# Tests
test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

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
def test_part1(input_data: str, expected: int) -> None:
    assert part1(input_data) == expected


# Part 2 test
# @pytest.mark.parametrize(("input_data", "expected"), ((test_data, 0),))
# def test_f(input_data: list[int], expected: int) -> None:
#    assert f(input_data) == expected
