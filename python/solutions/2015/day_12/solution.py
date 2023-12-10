# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/12

import json
import re

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2015
    _day = 12

    NUMBER_REGEX = re.compile(r"(-?\d+)")

    def sum_obj(self, obj):
        if isinstance(obj, list):
            return sum((self.sum_obj(o) for o in obj))
        elif isinstance(obj, dict):
            if any((v == "red" for v in obj.values())):
                return 0
            else:
                return sum((self.sum_obj(v) for v in obj.values()))
        elif isinstance(obj, int):
            return obj
        else:
            return 0

    @answer(119433)
    def part_1(self) -> int:
        return sum(map(int, self.NUMBER_REGEX.findall(self.input)))

    @answer(68466)
    def part_2(self) -> int:
        obj = json.loads(self.input)
        return self.sum_obj(obj)
