# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    NUMBER_REGEX = re.compile(r"(\d+)")
    SYMBOL_REGEX = re.compile(r"[^\d\.\s]")
    STAR_REGEX = re.compile(r"\*")

    @classmethod
    def get_range(cls, vec, imin, imax, inclusive=False):
        return vec[max(0, imin): min(len(vec) - 1, imax) + 1 if inclusive else min(len(vec), imax)]

    def is_symbol_adjacent(self, line_idx, span):
        return any(map(lambda line: self.SYMBOL_REGEX.search(self.get_range(line, span[0] - 1, span[1] + 1)),
                       self.get_range(self.input, line_idx - 1, line_idx + 1, inclusive=True)))

    def adjacent_numbers(self, line_idx, col_idx):
        return sum(
            ([int(c.group()) for c in self.NUMBER_REGEX.finditer(line) if c.start() - 1 <= col_idx < c.end() + 1]
             for line in self.get_range(self.input, line_idx - 1, line_idx + 1, inclusive=True)), [])

    @answer(539433)
    def part_1(self) -> int:
        result = 0
        for i, line in enumerate(self.input):
            for c in self.NUMBER_REGEX.finditer(line):
                if self.is_symbol_adjacent(i, c.span()):
                    result += int(c.group())
        return result

    @answer(75847567)
    def part_2(self) -> int:
        result = 0
        for i, line in enumerate(self.input):
            for c in self.STAR_REGEX.finditer(line):
                numbers = self.adjacent_numbers(i, c.start())
                if len(numbers) == 2:
                    result += numbers[0] * numbers[1]
        return result
