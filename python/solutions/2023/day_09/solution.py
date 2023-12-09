# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/9

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    @answer((2008960228, 1097))
    def solve(self) -> tuple[int, int]:
        total1, total2 = 0, 0
        for line in self.input:
            numbers = np.array([int(x) for x in line.split()])
            factor = 1
            while np.any(numbers):
                total1 += numbers[-1]
                total2 += factor * numbers[0]
                factor *= -1
                numbers = np.diff(numbers)
        return total1, total2
