# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/12

import re
from functools import cache

from tqdm import tqdm

from ...base import StrSplitSolution, answer
from ...utils.misc import split_lengths


class Solution(StrSplitSolution):
    _year = 2023
    _day = 12

    SHORTEN_REGEX = re.compile(r"(\.*)(#+)\.")

    @cache
    def count_arrangements(self, conditions, runs):
        if '?' in conditions:
            m = re.match(self.SHORTEN_REGEX, conditions)
            if m is not None:
                if len(runs) == 0 or m.end(2) - m.start(2) != runs[0]:
                    return 0
                conditions = conditions[m.end(2):]
                runs = runs[1:]
            return (self.count_arrangements(conditions.replace('?', '.', 1), runs) +
                    self.count_arrangements(conditions.replace('?', '#', 1), runs))
        else:
            cur_runs = tuple(split_lengths(conditions, '.', return_empty=False))
            return cur_runs == runs

    @answer((7361, 83317216247365))
    def solve(self) -> tuple[int, int]:
        total1, total2 = 0, 0
        for line in tqdm(self.input):
            conditions, runs = line.split()
            runs = tuple(map(int, runs.split(",")))
            total1 += self.count_arrangements(conditions, runs)
            total2 += self.count_arrangements('?'.join([conditions] * 5), runs * 5)
        return total1, total2
