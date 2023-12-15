# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

import re

from ...base import StrSplitSolution, answer
from ...utils.relaxed import relaxed_str_list
from ...utils.misc import index_iter


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    NUMBER_REGEX = re.compile(r"(\d+)")
    SYMBOL_REGEX = re.compile(r"[^\d\.\s]")

    @classmethod
    def is_symbol_adjacent(cls, lines, line_idx, span):
        return any(
            map(lambda line: cls.SYMBOL_REGEX.search(line[span[0] - 1:span[1] + 1]), lines[line_idx - 1:line_idx + 2]))

    @classmethod
    def adjacent_numbers(cls, lines, line_idx, col_idx):
        return sum(
            ([int(c.group()) for c in cls.NUMBER_REGEX.finditer(line) if c.start() - 1 <= col_idx < c.end() + 1]
             for line in lines[line_idx - 1:line_idx + 2]), [])

    @answer((539433, 75847567))
    def solve(self) -> tuple[int, int]:
        lines = relaxed_str_list(self.input)
        total1, total2 = 0, 0
        for i, line in enumerate(lines):
            for c in index_iter(line, '*'):
                numbers = self.adjacent_numbers(lines, i, c)
                if len(numbers) == 2:
                    total2 += numbers[0] * numbers[1]
            for c in self.NUMBER_REGEX.finditer(line):
                if self.is_symbol_adjacent(lines, i, c.span()):
                    total1 += int(c.group())
        return total1, total2
