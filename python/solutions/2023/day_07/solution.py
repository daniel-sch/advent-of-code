# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/7

from collections import Counter
from enum import IntEnum
from functools import total_ordering

from ...base import StrSplitSolution, answer


@total_ordering
class Hand:
    CARD_ORDER_NORMAL = "23456789TJQKA"
    CARD_ORDER_JOKERS = "J23456789TQKA"

    class HandType(IntEnum):
        HIGH_CARD = 0
        ONE_PAIR = 1
        TWO_PAIR = 2
        THREE_OF_A_KIND = 3
        FULL_HOUSE = 4
        FOUR_OF_A_KIND = 5
        FIVE_OF_A_KIND = 6

    def __init__(self, cards, jokers):
        self.card_string = cards
        card_order = self.CARD_ORDER_JOKERS if jokers else self.CARD_ORDER_NORMAL
        self.cards = [card_order.index(c) for c in cards]
        self.hand_type = self._determine_type(cards, jokers)

    def _determine_type(self, cards, jokers):
        c = Counter(cards)
        c['x'] = 0  # Make sure there are at least 2 entries
        if jokers:
            n_jokers = c['J']
            c['J'] = 0
            c[c.most_common(1)[0][0]] += n_jokers
        match list(map(lambda x: x[1], c.most_common(2))):
            case 5, _:
                return self.HandType.FIVE_OF_A_KIND
            case 4, _:
                return self.HandType.FOUR_OF_A_KIND
            case 3, 2:
                return self.HandType.FULL_HOUSE
            case 3, _:
                return self.HandType.THREE_OF_A_KIND
            case 2, 2:
                return self.HandType.TWO_PAIR
            case 2, _:
                return self.HandType.ONE_PAIR
            case 1, _:
                return self.HandType.HIGH_CARD

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            return self.cards < other.cards
        else:
            return self.hand_type < other.hand_type

    def __repr__(self):
        return f"{self.card_string} ({self.hand_type})"


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    @answer(248569531)
    def part_1(self) -> int:
        cards = list(map(lambda x: (Hand(x.split()[0], False), int(x.split()[1])), self.input))
        return sum(map(lambda x: x[0] * x[1][1], enumerate(sorted(cards), 1)))

    @answer(250382098)
    def part_2(self) -> int:
        cards = list(map(lambda x: (Hand(x.split()[0], True), int(x.split()[1])), self.input))
        return sum(map(lambda x: x[0] * x[1][1], enumerate(sorted(cards), 1)))
