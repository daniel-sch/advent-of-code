# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/4

from ...base import TextSolution, answer, slow
from hashlib import md5


class Solution(TextSolution):
    _year = 2015
    _day = 4

    def find_number(self, num_zeros):
        i = 0
        while True:
            if md5((self.input + str(i)).encode('ascii'), usedforsecurity=False).hexdigest().startswith(
                    "0" * num_zeros):
                return i
            i += 1

    @slow
    @answer(282749)
    def part_1(self) -> int:
        return self.find_number(5)

    @slow
    @answer(9962624)
    def part_2(self) -> int:
        return self.find_number(6)
