# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/6

import re

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 6

    LINE_REGEX = re.compile(r"(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)")

    @answer((400410, 15343601))
    def solve(self) -> tuple[int, int]:
        lights1 = np.zeros((1000, 1000), dtype=bool)
        lights2 = np.zeros((1000, 1000), dtype=int)
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            idx = np.s_[int(m.group(2)):int(m.group(4)) + 1, int(m.group(3)):int(m.group(5)) + 1]
            match m.group(1):
                case "turn on":
                    lights1[idx] = True
                    lights2[idx] += 1
                case "turn off":
                    lights1[idx] = False
                    lights2[idx] -= 1
                    lights2[lights2 < 0] = 0
                case "toggle":
                    lights1[idx] = ~lights1[idx]
                    lights2[idx] += 2
        return np.sum(lights1), np.sum(lights2)
