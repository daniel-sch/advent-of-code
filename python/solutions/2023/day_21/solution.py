# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/21

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 21

    def get_start_pos(self):
        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char == 'S':
                    return x, y

    @answer(3820)
    def part_1(self) -> int:
        positions = {self.get_start_pos()}
        rocks = np.array([[c == '#' for c in line] for line in self.input], dtype=bool)
        for _ in range(64):
            new_positions = set()
            for pos in positions:
                for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                    if (0 <= new_pos[0] < rocks.shape[1] and 0 <= new_pos[1] < rocks.shape[0] and
                            not rocks[new_pos[1], new_pos[0]]):
                        new_positions.add(new_pos)
            positions = new_positions
        return len(positions)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
