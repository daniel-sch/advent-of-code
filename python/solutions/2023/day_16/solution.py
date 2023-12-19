# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/16

import numpy as np

from ...base import StrSplitSolution, answer
from ...utils.arithmetic_tuple import AT


class Solution(StrSplitSolution):
    _year = 2023
    _day = 16

    def count_energized(self, start_beam):
        active_beams = [start_beam]
        energized = np.zeros((len(self.input), len(self.input[0])), dtype=bool)
        visited = set()
        while len(active_beams) > 0:
            cur_pos, cur_dir = active_beams.pop()
            if (cur_pos, cur_dir) in visited:
                continue
            else:
                visited.add((cur_pos, cur_dir))
            next_pos = cur_pos + cur_dir
            if not (0 <= next_pos[0] < len(self.input[0]) and 0 <= next_pos[1] < len(self.input)):
                continue
            energized[next_pos[1], next_pos[0]] = True
            match self.input[next_pos[1]][next_pos[0]], cur_dir:
                case ('.', _) | ('-', (1 | -1, 0)) | ('|', (0, 1 | -1)):
                    active_beams.append((next_pos, cur_dir))
                case '/', _:
                    active_beams.append((next_pos, AT((-cur_dir[1], -cur_dir[0]))))
                case '\\', _:
                    active_beams.append((next_pos, AT((cur_dir[1], cur_dir[0]))))
                case '|', _:
                    active_beams.append((next_pos, AT((0, -1))))
                    active_beams.append((next_pos, AT((0, 1))))
                case '-', _:
                    active_beams.append((next_pos, AT((-1, 0))))
                    active_beams.append((next_pos, AT((1, 0))))
        return np.sum(energized)

    @answer(6795)
    def part_1(self) -> int:
        return self.count_energized((AT((-1, 0)), AT((1, 0))))

    @answer(7154)
    def part_2(self) -> int:
        start_beams = [(AT((-1, y)), AT((1, 0))) for y in range(len(self.input))] + \
                      [(AT((len(self.input[0]), y)), AT((-1, 0))) for y in range(len(self.input))] + \
                      [(AT((x, -1)), AT((0, 1))) for x in range(len(self.input[0]))] + \
                      [(AT((x, len(self.input[0]))), AT((0, -1))) for x in range(len(self.input[0]))]
        return max(map(self.count_energized, start_beams))
