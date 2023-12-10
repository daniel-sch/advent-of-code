# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/9

import re

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 9

    LINE_REGEX = re.compile(r"(\w+) to (\w+) = (\d+)")

    def parse(self):
        cities = set()
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            cities.add(m[1])
            cities.add(m[2])
        cities = list(cities)
        connections = np.zeros((len(cities), len(cities)), dtype=int)
        for line in self.input:
            m = self.LINE_REGEX.match(line)
            connections[cities.index(m[1]), cities.index(m[2])] = int(m[3])
            connections[cities.index(m[2]), cities.index(m[1])] = int(m[3])
        return connections

    def tsp_step(self, con, cur_len, cur_pos, visited, best, dummy):
        if np.all(visited):
            return cur_len
        results = []
        for i in np.where(~visited)[0]:
            if con[cur_pos, i]:
                new_visited = visited.copy()
                new_visited[i] = True
                results.append(self.tsp_step(con, cur_len + con[cur_pos, i], i, new_visited, best, dummy))
        if len(results) == 0:
            return dummy
        else:
            return best(results)

    def solve_tsp(self, con, best, dummy):
        visited = np.zeros(con.shape[0], dtype=bool)
        results = []
        for i in range(len(visited)):
            new_visited = visited.copy()
            new_visited[i] = True
            results.append(self.tsp_step(con, 0, i, new_visited, best, dummy))
        return best(results)

    @answer(207)
    def part_1(self) -> int:
        connections = self.parse()
        return self.solve_tsp(connections, min, float("inf"))

    @answer(804)
    def part_2(self) -> int:
        connections = self.parse()
        return self.solve_tsp(connections, max, float("-inf"))
