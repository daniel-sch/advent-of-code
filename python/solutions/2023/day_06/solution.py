# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/6

import math

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    @classmethod
    def solve_race(cls, t, d):
        print(f"{t}, {d}")
        p = -t
        q = d + 1
        x1 = (-p - math.sqrt(p ** 2 - 4 * q)) / 2
        x2 = (-p + math.sqrt(p ** 2 - 4 * q)) / 2
        return math.floor(x2) - math.ceil(x1) + 1

    @answer(625968)
    def part_1(self) -> int:
        times = map(int, self.input[0].split(':')[1].split())
        distances = map(int, self.input[1].split(':')[1].split())
        return int(math.prod(map(lambda x: self.solve_race(*x), zip(times, distances))))

    @answer(43663323)
    def part_2(self) -> int:
        t = int(self.input[0].split(':')[1].replace(' ', ''))
        d = int(self.input[1].split(':')[1].replace(' ', ''))
        return int(self.solve_race(t, d))
