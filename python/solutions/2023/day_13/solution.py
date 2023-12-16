# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/13

from ...base import StrSplitSolution, answer
from ...utils.misc import split


class Solution(StrSplitSolution):
    _year = 2023
    _day = 13

    @classmethod
    def is_vertical_reflection(cls, pattern, i):
        errors = 0
        for x in range(i + 1):
            for y in range(len(pattern)):
                if i + x + 1 >= len(pattern[0]) or i - x < 0:
                    continue
                if pattern[y][i + x + 1] != pattern[y][i - x]:
                    errors += 1
        return errors

    @classmethod
    def vertical_reflections(cls, pattern, expected_errors):
        for i in range(len(pattern[0]) - 1):
            if cls.is_vertical_reflection(pattern, i) == expected_errors:
                return i + 1
        return 0

    @classmethod
    def is_horizontal_reflection(cls, pattern, i):
        errors = 0
        for x in range(len(pattern[0])):
            for y in range(i + 1):
                if i + y + 1 >= len(pattern) or i - y < 0:
                    continue
                if pattern[i + y + 1][x] != pattern[i - y][x]:
                    errors += 1
        return errors

    @classmethod
    def horizontal_reflections(cls, pattern, expected_errors):
        for i in range(len(pattern) - 1):
            if cls.is_horizontal_reflection(pattern, i) == expected_errors:
                return i + 1
        return 0

    @answer((37561, 31108))
    def solve(self) -> tuple[int, int]:
        total1, total2 = 0, 0
        for pattern in split(self.input, ''):
            total1 += self.vertical_reflections(pattern, 0) + 100 * self.horizontal_reflections(pattern, 0)
            total2 += self.vertical_reflections(pattern, 1) + 100 * self.horizontal_reflections(pattern, 1)
        return total1, total2
