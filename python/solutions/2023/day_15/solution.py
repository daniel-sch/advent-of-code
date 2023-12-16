# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/15

import re
from collections import defaultdict

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 15

    INSTRUCTION_REGEX = re.compile(r"([a-z]+)([\-=])(\d*)")

    @classmethod
    def hash(cls, text):
        cur = 0
        for c in text:
            cur = (cur + ord(c)) * 17 % 256
        return cur

    @answer(494980)
    def part_1(self) -> int:
        return sum(map(self.hash, self.input.split(',')))

    @answer(247933)
    def part_2(self) -> int:
        boxes = defaultdict(list)
        for instruction in self.input.split(','):
            m = self.INSTRUCTION_REGEX.match(instruction)
            label, operation, focal_length = m[1], m[2], int(m[3]) if m[3] else None
            box = boxes[self.hash(label)]
            match_idx = ([i for i, x in enumerate(box) if x[0] == label] or [None])[0]
            if operation == '-':
                if match_idx is not None:
                    del box[match_idx]
            else:
                if match_idx is not None:
                    box[match_idx] = (label, focal_length)
                else:
                    box.append((label, focal_length))

        total = 0
        for k, v in boxes.items():
            for i, x in enumerate(v):
                total += (k + 1) * (i + 1) * x[1]
        return total
