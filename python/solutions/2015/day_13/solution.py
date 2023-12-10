# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/13

import re
from itertools import permutations

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 13

    LINE_REGEX = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.")

    def compute(self, include_self):
        names = set()
        for line in self.input:
            names.add(self.LINE_REGEX.match(line)[1])
        if include_self:
            names.add("self")
        names = list(names)

        happiness_change = np.zeros((len(names), len(names)))
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            happiness_change[names.index(m[1]), names.index(m[4])] = (-1 if m[2] == "lose" else 1) * int(m[3])

        max_happiness = 0
        for order in permutations(range(len(names))):
            happiness = 0
            for i in range(len(order)):
                happiness += happiness_change[order[i], order[(i + 1) % len(order)]]
                happiness += happiness_change[order[(i + 1) % len(order)], order[i]]
            if happiness > max_happiness:
                max_happiness = happiness
        return int(max_happiness)

    @answer(733)
    def part_1(self) -> int:
        return self.compute(False)

    @answer(725)
    def part_2(self) -> int:
        return self.compute(True)
