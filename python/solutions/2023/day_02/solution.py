# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

import math
import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    MAX_CUBES = dict(red=12, green=13, blue=14)
    CUBE_REGEX = re.compile(r"(\d+) (\w+)")

    @classmethod
    def is_game_possible(cls, game_string):
        return all((cls.MAX_CUBES[c] >= int(n) for n, c in cls.CUBE_REGEX.findall(game_string)))

    @classmethod
    def fewest_cubes_prod(cls, game_string):
        min_cubes = dict(red=0, green=0, blue=0)
        for amount, color in cls.CUBE_REGEX.findall(game_string):
            min_cubes[color] = max(int(amount), min_cubes[color])
        return math.prod(min_cubes.values())

    @answer(2545)
    def part_1(self) -> int:
        return sum((i for i, line in enumerate(self.input, 1) if self.is_game_possible(line)))

    @answer(78111)
    def part_2(self) -> int:
        return sum((self.fewest_cubes_prod(line) for line in self.input))
