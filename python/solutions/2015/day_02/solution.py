# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 2

    @answer((1586300, 3737498))
    def solve(self) -> tuple[int, int]:
        total1, total2 = 0, 0
        for line in self.input:
            dims = sorted([int(x) for x in line.split('x')])
            total1 += 3 * dims[0] * dims[1] + 2 * dims[0] * dims[2] + 2 * dims[1] * dims[2]
            total2 += 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2]
        return total1, total2
