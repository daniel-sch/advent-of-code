# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/10

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2015
    _day = 10

    @classmethod
    def convert(cls, in_):
        result = []
        last = in_[0]
        count = 0
        for i in range(len(in_)):
            if in_[i] == last:
                count += 1
            else:
                result.append(str(count))
                result.append(last)
                last = in_[i]
                count = 1
        result.append(str(count))
        result.append(last)
        return result

    @answer((360154, 5103798))
    def solve(self) -> tuple[int, int]:
        result = self.input
        for i in range(40):
            result = self.convert(result)
        result1 = len(result)
        for i in range(10):
            result = self.convert(result)
        return result1, len(result)
