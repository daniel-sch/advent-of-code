# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/24

from ...base import StrSplitSolution, answer


class Blizzard:
    DIR_MAP = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}
    CHAR_MAP = {v: k for k, v in DIR_MAP.items()}

    def __init__(self, pos, char):
        self.pos = pos
        self.direction = self.DIR_MAP[char]

    def step(self):
        self.pos = ((self.pos[0] + self.direction[0]) % Field.width, (self.pos[1] + self.direction[1]) % Field.height)

    def __str__(self):
        return self.CHAR_MAP[self.direction]


class Field:
    width = None
    height = None

    def __init__(self, lines):
        Field.width = len(lines[0]) - 2
        Field.height = len(lines) - 2
        self.special_positions = [(0, -1), (Field.width - 1, Field.height)]
        self.target = None
        self.set_target('goal')
        self.possible_positions = {(0, -1)}
        self.steps = 0

        self.blizzards = []
        for y, line in enumerate(lines[1:-1]):
            for x, char in enumerate(line[1:-1]):
                if char != '.':
                    self.blizzards.append(Blizzard((x, y), char))

    def set_target(self, target):
        self.target = self.special_positions[1 if target == 'goal' else 0]

    def step(self):
        self.steps += 1
        blizzard_positions = set()
        for b in self.blizzards:
            b.step()
            blizzard_positions.add(b.pos)
        new_positions = set()
        for pos in self.possible_positions:
            for dx, dy in [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos == self.target:
                    self.possible_positions = {self.target}
                    return True
                if (new_pos in self.special_positions or (0 <= new_pos[0] < self.width and
                                                          0 <= new_pos[1] < self.height and
                                                          new_pos not in blizzard_positions)):
                    new_positions.add(new_pos)
        self.possible_positions = new_positions
        return False

    def __str__(self):
        field = [['.'] * self.width for _ in range(self.height)]
        for b in self.blizzards:
            x = field[b.pos[1]][b.pos[0]]
            if x == '.':
                x = str(b)
            elif x.isdigit():
                x = str(int(x) + 1)
            else:
                x = '2'
            field[b.pos[1]][b.pos[0]] = x
        for p in self.possible_positions:
            if 0 <= p[1] < self.height:  # Don't display initial position or target
                field[p[1]][p[0]] = 'E'
        return '\n'.join((''.join(line) for line in field))


class Solution(StrSplitSolution):
    _year = 2022
    _day = 24

    @answer((269, 825))
    def solve(self) -> tuple[int, int]:
        f = Field(self.input)
        while not f.step():
            self.debug(f"Minute {f.steps}\n{f}")
        result1 = f.steps
        f.set_target('start')
        while not f.step():
            self.debug(f"Minute {f.steps}\n{f}")
        f.set_target('goal')
        while not f.step():
            self.debug(f"Minute {f.steps}\n{f}")
        return result1, f.steps
