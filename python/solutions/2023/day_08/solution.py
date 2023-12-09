# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/8

import math
import re
from itertools import cycle

from ...base import StrSplitSolution, answer, slow


class Solution(StrSplitSolution):
    _year = 2023
    _day = 8

    LINE_REGEX = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

    def parse(self):
        self.movements = self.input[0]
        self.instructions = {}
        for line in self.input[2:]:
            m = self.LINE_REGEX.match(line)
            self.instructions[m[1]] = (m[2], m[3])

    def step(self, pos, move):
        if move == 'L':
            return self.instructions[pos][0]
        elif move == 'R':
            return self.instructions[pos][1]

    def find_cycle(self, start):
        hist = []
        end_indizes = []
        i = 0
        pos = start
        while (i % len(self.movements), pos) not in hist:
            if pos.endswith('Z'):
                end_indizes.append(i)
            hist.append((i % len(self.movements), pos))
            pos = self.step(pos, self.movements[i % len(self.movements)])
            i += 1
        cycle_start = hist.index((i % len(self.movements), pos))
        cycle_length = i - cycle_start
        assert len(end_indizes) == 1
        assert end_indizes[0] == cycle_length
        return cycle_length

    @answer(11309)
    def part_1(self) -> int:
        self.parse()
        pos = "AAA"
        for i, move in enumerate(cycle(self.movements), 1):
            pos = self.step(pos, move)
            if pos == "ZZZ":
                return i

    @slow
    @answer(13740108158591)
    def part_2(self) -> int:
        self.parse()
        pos = [p for p in self.instructions.keys() if p.endswith('A')]
        cycles = list(map(self.find_cycle, pos))
        return math.lcm(*cycles)
