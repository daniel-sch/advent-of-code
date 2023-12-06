# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/8

from ast import literal_eval

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 8

    @answer(1371)
    def part_1(self) -> int:
        result = 0
        for line in self.input:
            line_eval = literal_eval(line)
            result += len(line) - len(line_eval)
        return result

    # @answer(1234)
    def part_2(self) -> int:
        result = 0
        for line in self.input:
            line_escaped = repr(line.replace('"', "'") + '"')  # ugly hack to convince repr to escape the "
            result += len(line_escaped) - len(line) - 1
        return result
