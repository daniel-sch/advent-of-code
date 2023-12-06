# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    LINE_REGEX = re.compile(r".*: (.*) \| (.*)")

    @answer(20667)
    def part_1(self) -> int:
        result = 0
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            winning_numbers = {int(x) for x in m.group(1).split()}
            own_numbers = {int(x) for x in m.group(2).split()}
            intersect = len(winning_numbers & own_numbers)
            if intersect:
                result += 2 ** (intersect - 1)
        return result

    @answer(5833065)
    def part_2(self) -> int:
        card_wins = []
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            winning_numbers = {int(x) for x in m.group(1).split()}
            own_numbers = {int(x) for x in m.group(2).split()}
            card_wins.append(len(winning_numbers & own_numbers))
        card_count = [1] * len(card_wins)
        for i, card_win in enumerate(card_wins):
            for j in range(min(i + 1, len(card_wins)), min(card_win + i, len(card_wins)) + 1):
                card_count[j] += card_count[i]
        return sum(card_count)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
