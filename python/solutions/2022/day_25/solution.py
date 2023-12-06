# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/25

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 25

    SNAFU_MAP = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
    INT_MAP = {v: k for k, v in SNAFU_MAP.items()}

    @classmethod
    def snafu_to_int(cls, snafu):
        total = 0
        for i, d in enumerate(map(lambda x: cls.SNAFU_MAP[x], reversed(snafu))):
            total += d * 5 ** i
        return total

    @classmethod
    def int_to_snafu(cls, number):
        digits = []
        while number > 0:
            digits.append(number % 5)
            number //= 5
        carry = 0
        for i in range(len(digits)):
            digits[i] += carry
            if digits[i] > 2:
                digits[i] -= 5
                carry = 1
            else:
                carry = 0
        if carry:
            digits.append(carry)
        return "".join(map(lambda x: cls.INT_MAP[x], reversed(digits)))

    @answer("122-12==0-01=00-0=02")
    def part_1(self) -> str:
        total = 0
        for line in self.input:
            total += self.snafu_to_int(line)
        self.int_to_snafu(total)
        return self.int_to_snafu(total)

    # @answer(1234)
    def part_2(self) -> int:
        pass
