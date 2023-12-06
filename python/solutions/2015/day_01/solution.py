# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/1

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2015
    _day = 1

    @answer(280)
    def part_1(self) -> int:
        return self.input.count("(") - self.input.count(")")

    @answer(1797)
    def part_2(self) -> int:
        floor = 0
        for pos, char in enumerate(self.input, 1):
            floor += 1 if char == "(" else -1
            if floor == -1:
                return pos
