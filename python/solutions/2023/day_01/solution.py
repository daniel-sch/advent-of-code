# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1
import re

from ...base import StrSplitSolution, answer

NUMBERS = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "one", "two", "three", "four", "five", "six",
           "seven", "eight", "nine"]
FIRST_NUMBER_REGEX = re.compile(f"({'|'.join(NUMBERS)})")
LAST_NUMBER_REGEX = re.compile(f"(?s:.*)({'|'.join(NUMBERS)})")


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(56108)
    def part_1(self) -> int:
        result = 0
        for line in self.input:
            numbers = [int(c) for c in line if c.isdigit()]
            result += numbers[0] * 10 + numbers[-1]
        return result

    @answer(55652)
    def part_2(self) -> int:
        result = 0
        for line in self.input:
            first_number = FIRST_NUMBER_REGEX.search(line).group(1)
            last_number = LAST_NUMBER_REGEX.search(line).group(1)
            result += NUMBERS.index(first_number) % 10 * 10 + NUMBERS.index(last_number) % 10
        return result
