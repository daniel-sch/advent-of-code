# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/14

import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 14

    LINE_REGEX = re.compile(r"\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.")

    def compute_reindeer(self, line):
        m = self.LINE_REGEX.match(line)
        speed, travel_duration, rest_duration = int(m[1]), int(m[2]), int(m[3])
        remaining_time = 2503
        distance_traveled = 0
        while remaining_time > 0:
            travel_time = min(travel_duration, remaining_time)
            remaining_time -= travel_time
            distance_traveled += speed * travel_time
            remaining_time -= rest_duration
        return distance_traveled

    @answer(2655)
    def part_1(self) -> int:
        return max(map(self.compute_reindeer, self.input))

    @answer(1059)
    def part_2(self) -> int:
        remaining_time = 2503
        reindeers = []
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            speed, travel_duration, rest_duration = int(m[1]), int(m[2]), int(m[3])
            reindeers.append(dict(speed=speed, travel_duration=travel_duration, rest_duration=rest_duration,
                                  remaining_travel_time=travel_duration, remaining_rest_time=rest_duration, distance=0,
                                  points=0))
        for i in range(remaining_time):
            for reindeer in reindeers:
                if reindeer['remaining_travel_time'] > 0:
                    reindeer['remaining_travel_time'] -= 1
                    reindeer['distance'] += reindeer['speed']
                elif reindeer['remaining_rest_time'] > 0:
                    reindeer['remaining_rest_time'] -= 1
                else:
                    reindeer['remaining_travel_time'] = reindeer['travel_duration'] - 1
                    reindeer['remaining_rest_time'] = reindeer['rest_duration']
                    reindeer['distance'] += reindeer['speed']
            best = max(map(lambda x: x['distance'], reindeers))
            for reindeer in reindeers:
                if reindeer['distance'] == best:
                    reindeer['points'] += 1
        return max(map(lambda x: x['points'], reindeers))
