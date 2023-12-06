# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/5

import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 5

    FORBIDDEN_REGEX = re.compile(r"ab|cd|pq|xy")
    VOWEL_REGEX = re.compile(r"[aeiou]")
    DOUBLE_REGEX = re.compile(r"(.)\1")
    DOUBLEDOUBLE_REGEX = re.compile(r"(..).*\1")
    REPEATS_REGEX = re.compile(r"(.).\1")

    @answer(238)
    def part_1(self) -> int:
        def is_nice(line):
            return self.FORBIDDEN_REGEX.search(line) is None \
                and len(self.VOWEL_REGEX.findall(line)) >= 3 \
                and self.DOUBLE_REGEX.search(line) is not None

        return sum((is_nice(line) for line in self.input))

    @answer(69)
    def part_2(self) -> int:
        def is_nice(line):
            return self.DOUBLEDOUBLE_REGEX.search(line) is not None and self.REPEATS_REGEX.search(line) is not None

        return sum((is_nice(line) for line in self.input))
