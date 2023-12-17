# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/14

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14

    def parse(self):
        cube_rocks = np.zeros((len(self.input), len(self.input[0])), dtype=bool)
        round_rocks = np.zeros((len(self.input), len(self.input[0])), dtype=bool)
        for y, line in enumerate(self.input):
            for x, c in enumerate(line):
                if c == '#':
                    cube_rocks[y, x] = True
                elif c == 'O':
                    round_rocks[y, x] = True
        return cube_rocks, round_rocks

    @classmethod
    def shift_north(cls, cube_rocks, round_rocks):
        new_round_rocks = np.zeros_like(round_rocks)
        for x in range(cube_rocks.shape[1]):
            shifting_to = 0
            for y in range(cube_rocks.shape[0]):
                if cube_rocks[y, x]:
                    shifting_to = y + 1
                elif round_rocks[y, x]:
                    new_round_rocks[shifting_to, x] = True
                    shifting_to += 1
        return new_round_rocks

    @classmethod
    def compute_load(cls, round_rocks):
        total = 0
        for x in range(round_rocks.shape[1]):
            for y in range(round_rocks.shape[0]):
                if round_rocks[y, x]:
                    total += round_rocks.shape[0] - y
        return total

    @classmethod
    def print(cls, cube_rocks, round_rocks):
        for x in range(round_rocks.shape[0]):
            for y in range(round_rocks.shape[1]):
                if cube_rocks[x, y]:
                    print('#', end='')
                elif round_rocks[x, y]:
                    print('O', end='')
                else:
                    print('.', end='')
            print()
        print()

    @answer(108840)
    def part_1(self) -> int:
        cube_rocks, round_rocks = self.parse()
        round_rocks = self.shift_north(cube_rocks, round_rocks)
        return self.compute_load(round_rocks)

    @answer(103445)
    def part_2(self) -> int:
        cube_rocks, round_rocks = self.parse()
        cube_rocks_rotations = [cube_rocks, np.rot90(cube_rocks, -1), np.rot90(cube_rocks, -2),
                                np.rot90(cube_rocks, -3)]
        cycle_cache = dict()
        max_rounds = 1000000000
        remaining_rounds = None
        for cur_round in range(max_rounds):
            if remaining_rounds is None:
                cur_hash = hash(round_rocks.data.tobytes())
                if cur_hash in cycle_cache:
                    print(f"Cycle found from {cycle_cache[cur_hash]} to {cur_round}")
                    remaining_rounds = (max_rounds - cur_round) % (cur_round - cycle_cache[cur_hash])
                else:
                    cycle_cache[cur_hash] = cur_round
            if remaining_rounds is not None:
                if remaining_rounds == 0:
                    break
                else:
                    remaining_rounds -= 1

            for rotation in range(4):
                round_rocks = self.shift_north(cube_rocks_rotations[rotation], round_rocks)
                round_rocks = np.rot90(round_rocks, -1)
        return self.compute_load(round_rocks)
