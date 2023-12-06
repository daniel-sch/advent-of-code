# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

import re

from ...base import StrSplitSolution, answer
from ...utils.relaxed import RelaxList


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    LINE_REGEX = re.compile(r".*: (.*) \| (.*)")

    @answer((20667, 5833065))
    def solve(self) -> tuple[int, int]:
        total1 = 0
        card_count = RelaxList([1] * len(self.input))
        for i, line in enumerate(self.input):
            m = self.LINE_REGEX.match(line)
            winning_numbers = {int(x) for x in m.group(1).split()}
            own_numbers = {int(x) for x in m.group(2).split()}
            card_win = len(winning_numbers & own_numbers)
            if card_win:
                total1 += 2 ** (card_win - 1)
            for j in range(card_win):
                card_count[i + j + 1] += card_count[i]
        return total1, sum(card_count)
