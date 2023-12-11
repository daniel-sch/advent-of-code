# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/11

from itertools import combinations

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    def parse(self):
        galaxies = []
        for y, line in enumerate(self.input):
            for x, c in enumerate(line):
                if c == '#':
                    galaxies.append((x, y))
        empty_cols = set(range(len(self.input[0]))) - set((x for x, y in galaxies))
        empty_rows = set(range(len(self.input))) - set((y for x, y in galaxies))
        return galaxies, empty_rows, empty_cols

    @answer((9418609, 593821230983))
    def solve(self) -> tuple[int, int]:
        galaxies, empty_rows, empty_cols = self.parse()
        direct_dists, traversed_empty_rows_cols = 0, 0
        for first, second in combinations(galaxies, 2):
            x_range = set(range(min(first[0], second[0]), max(first[0], second[0])))
            y_range = set(range(min(first[1], second[1]), max(first[1], second[1])))
            direct_dists += len(x_range) + len(y_range)
            traversed_empty_rows_cols += len(x_range & empty_cols) + len(y_range & empty_rows)
        return direct_dists + traversed_empty_rows_cols, direct_dists + 999999 * traversed_empty_rows_cols
