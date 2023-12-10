# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/11

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2015
    _day = 11

    LETTERS = "abcdefghijklmnopqrstuvwxyz"
    LETTER_MAP = {k: i for i, k in enumerate(LETTERS)}
    LETTER_INV_MAP = {i: k for i, k in enumerate(LETTERS)}

    @classmethod
    def inc_string(cls, passwd):
        for i in range(len(passwd)):
            x = passwd[-i - 1] + 1
            passwd[-i - 1] = x % len(cls.LETTERS)
            if x < len(cls.LETTERS):
                break
        return passwd

    @classmethod
    def contains_straight(cls, passwd):
        for i in range(len(passwd) - 2):
            if passwd[i] == passwd[i + 1] - 1 == passwd[i + 2] - 2:
                return True
        return False

    @classmethod
    def contains_illegal(cls, passwd):
        return 8 in passwd or 11 in passwd or 14 in passwd

    @classmethod
    def contains_doubles(cls, passwd):
        i = 0
        doubles = 0
        while i < len(passwd) - 1:
            if passwd[i] == passwd[i + 1]:
                doubles += 1
                i += 1
            i += 1
        return doubles >= 2

    @classmethod
    def check_rules(cls, passwd):
        return cls.contains_straight(passwd) and not cls.contains_illegal(passwd) and cls.contains_doubles(passwd)

    @classmethod
    def next_passwd(cls, passwd):
        passwd = cls.inc_string(passwd)
        while not cls.check_rules(passwd):
            passwd = cls.inc_string(passwd)
        return passwd

    @answer(("vzbxxyzz", "vzcaabcc"))
    def solve(self) -> tuple[str, str]:
        passwd = [self.LETTER_MAP[c] for c in self.input]
        passwd = self.next_passwd(passwd)
        passwd1 = ''.join((self.LETTER_INV_MAP[c] for c in passwd))
        passwd = self.next_passwd(passwd)
        passwd2 = ''.join((self.LETTER_INV_MAP[c] for c in passwd))
        return passwd1, passwd2
