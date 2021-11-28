# What to do
import pytest


def main(filename:str) -> int:
    with open(filename) as inputData:
        rawData = inputData.readlines()

    return 0


if __name__ == '__main__':
    raise SystemExit(main('Inputs_1/day1.txt'))


#Tests

