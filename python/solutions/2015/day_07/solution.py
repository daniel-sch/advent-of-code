# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/7

import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2015
    _day = 7

    LINE_REGEX = re.compile(r"(\w+)?? ?([A-Z]+)? ?(\w+) -> ([a-z]+)")
    UNARY_OPERATORS = [None, "NOT"]

    @classmethod
    def parse_value(cls, signals, in_):
        if in_:
            if in_.isdigit():
                return int(in_)
            elif in_ in signals:
                return signals[in_]
        return None

    @classmethod
    def compute_gate(cls, op, first, second):
        match op:
            case None:
                return second
            case "NOT":
                return ~second
            case "AND":
                return first & second
            case "OR":
                return first | second
            case "LSHIFT":
                return first << second
            case "RSHIFT":
                return first >> second
            case _:
                assert False, f"Unknown op {op}"

    @classmethod
    def to_uint16(cls, x):
        return x & 0xFFFF

    @classmethod
    def compute_all(cls, lines, signals):
        while len(lines):
            new_lines = []
            for line in lines:
                m = cls.LINE_REGEX.match(line)
                if m.group(4) in signals:
                    continue
                first_value = cls.parse_value(signals, m.group(1))
                second_value = cls.parse_value(signals, m.group(3))
                if (m.group(2) not in cls.UNARY_OPERATORS and first_value is None) or second_value is None:
                    new_lines.append(line)
                else:
                    signals[m.group(4)] = cls.to_uint16(cls.compute_gate(m.group(2), first_value, second_value))
            lines = new_lines
        return signals

    @answer((956, 40149))
    def solve(self) -> tuple[int, int]:
        signals1 = self.compute_all(self.input, dict())
        signals2 = self.compute_all(self.input, dict(b=signals1['a']))
        return signals1['a'], signals2['a']
