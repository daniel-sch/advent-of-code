# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/3

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2015
    _day = 3

    @classmethod
    def process_santa(cls, visited, instr):
        x, y = 0, 0
        for c in instr:
            match c:
                case '>':
                    x += 1
                case '<':
                    x -= 1
                case '^':
                    y += 1
                case 'v':
                    y -= 1
            visited.add((x, y))

    @answer(2565)
    def part_1(self) -> int:
        visited = {(0, 0)}
        self.process_santa(visited, self.input)
        return len(visited)

    @answer(2639)
    def part_2(self) -> int:
        visited = {(0, 0)}
        self.process_santa(visited, self.input[::2])
        self.process_santa(visited, self.input[1::2])
        return len(visited)
