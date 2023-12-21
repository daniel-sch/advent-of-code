# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/19

import re

from ...base import StrSplitSolution, answer
from ...utils.misc import split


class Solution(StrSplitSolution):
    _year = 2023
    _day = 19

    PART_REGEX = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
    RULES_REGEX = re.compile(r"([a-z]+){(.*)}")
    RULE_REGEX = re.compile(r"(([xmas])([<>])(\d+):)?([a-zAR]+)")  #

    def parse(self):
        workflows_str, self.parts = split(self.input, '')
        self.workflows = {}
        for rule in workflows_str:
            m = self.RULES_REGEX.match(rule)
            self.workflows[m[1]] = str(m[2]).split(',')

    @answer(350678)
    def part_1(self) -> int:
        self.parse()
        total = 0
        for part_str in self.parts:
            m = self.PART_REGEX.match(part_str)
            part = dict(x=int(m[1]), m=int(m[2]), a=int(m[3]), s=int(m[4]))
            workflow = "in"
            while True:
                if workflow == "A":
                    total += sum(part.values())
                    break
                if workflow == "R":
                    break
                for rule in self.workflows[workflow]:
                    m = self.RULE_REGEX.match(rule)
                    if m[1]:
                        if m[3] == '<' and part[m[2]] < int(m[4]) or m[3] == '>' and part[m[2]] > int(m[4]):
                            workflow = m[5]
                            break
                    else:
                        workflow = m[5]
        return total

    def get_volume(self, workflow, conditions):
        if workflow == "A":
            return (conditions['max_x'] - conditions['min_x'] + 1) * (conditions['max_m'] - conditions['min_m'] + 1) * \
                (conditions['max_a'] - conditions['min_a'] + 1) * (conditions['max_s'] - conditions['min_s'] + 1)
        if workflow == "R":
            return 0
        total = 0
        for rule in self.workflows[workflow]:
            m = self.RULE_REGEX.match(rule)
            if m[1]:
                sub_conditions = conditions.copy()
                if m[3] == '<':
                    conditions[f'min_{m[2]}'] = int(m[4])
                    sub_conditions[f'max_{m[2]}'] = int(m[4]) - 1
                else:
                    conditions[f'max_{m[2]}'] = int(m[4])
                    sub_conditions[f'min_{m[2]}'] = int(m[4]) + 1
                total += self.get_volume(m[5], sub_conditions)
            else:
                total += self.get_volume(m[5], conditions)
        return total

    # @answer(1234)
    def part_2(self) -> int:
        conditions = dict(min_x=1, max_x=4000, min_m=1, max_m=4000, min_a=1, max_a=4000, min_s=1, max_s=4000)
        return self.get_volume("in", conditions)
