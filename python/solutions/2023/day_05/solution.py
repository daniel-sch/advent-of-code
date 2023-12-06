# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 5

    @classmethod
    def consolidate_ranges(cls, ranges):
        ranges = sorted(ranges, key=lambda x: x[0])
        i = 0
        while i < len(ranges) - 1:
            if ranges[i][0] + ranges[i][1] >= ranges[i + 1][0]:
                range_i_stop = ranges[i][0] + ranges[i][1]
                range_i1_stop = ranges[i + 1][0] + ranges[i + 1][1]
                ranges[i] = (ranges[i][0], max(range_i_stop, range_i1_stop) - ranges[i][0])
                del ranges[i + 1]
            else:
                i += 1
        return ranges

    @classmethod
    def map_range(cls, range_, mapping):
        range_start, range_stop = range_[0], range_[0] + range_[1]
        mapping_start, mapping_stop, mapping_delta = mapping[1], mapping[1] + mapping[2], mapping[0] - mapping[1]

        leftover_ranges = []
        mapped_range = []
        if range_start < mapping_start:  # part of range that is left of mapping
            start = range_start
            leftover_ranges.append((start, min(range_stop, mapping_start) - start))
        if max(range_start, mapping_start) < min(range_stop, mapping_stop):  # overlapping part will be mapped
            start = max(range_start, mapping_start)
            stop = min(range_stop, mapping_stop)
            mapped_range.append((start + mapping_delta, stop - start))
        if range_stop > mapping_stop:  # part of range that is right of mapping
            start = max(mapping_stop, range_start)
            leftover_ranges.append((start, range_stop - start))
        return leftover_ranges, mapped_range

    @answer(51580674)
    def part_1(self) -> int:
        seeds = [int(x) for x in self.input[0].split(": ")[1].split()]
        new_seeds = seeds
        for line in self.input[1:]:
            if len(line) == 0:  # new map starts
                seeds = new_seeds
                new_seeds = seeds.copy()
            elif line[0].isdigit():  # new line for map
                mapping = [int(x) for x in line.split()]
                for i, s in enumerate(seeds):
                    if 0 <= s - mapping[1] < mapping[2]:
                        new_seeds[i] = s + mapping[0] - mapping[1]
        return min(new_seeds)

    @answer(99751240)
    def part_2(self) -> int:
        seeds = [int(x) for x in self.input[0].split(": ")[1].split()]
        leftover_ranges = list(zip(seeds[::2], seeds[1::2]))
        mapped_ranges = []
        for line in self.input[1:]:
            if len(line) == 0:  # new map starts
                leftover_ranges = self.consolidate_ranges(leftover_ranges + mapped_ranges)
                mapped_ranges = []
            elif line[0].isdigit():  # new line for map
                mapping = [int(x) for x in line.split()]
                temp_ranges = []
                for r in leftover_ranges:
                    l, m = self.map_range(r, mapping)
                    temp_ranges += l
                    mapped_ranges += m
                leftover_ranges = temp_ranges
        return min((x[0] for x in leftover_ranges + mapped_ranges))
