# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/10

from enum import Enum, auto

from ...base import StrSplitSolution, answer
from ...utils.arithmetic_tuple import AT
from ...utils.relaxed import relaxed_str_list


class Solution(StrSplitSolution):
    _year = 2023
    _day = 10

    def init(self):
        self.MOVES = ["|NS", "-EW", "LNE", "JNW", "7SW", "FSE"]
        self.DIR_MAP = {"N": AT((0, -1)), "S": AT((0, 1)), "W": AT((-1, 0)), "E": AT((1, 0))}
        self.MOVE_MAP = {x[0]: (self.DIR_MAP[x[1]], self.DIR_MAP[x[2]]) for x in self.MOVES}
        self.START_MOVES = [(AT((0, -1)), ("|", "7", "F")), (AT((0, 1)), ("|", "L", "J")),
                            (AT((-1, 0)), ("-", "L", "F")), (AT((1, 0)), ("-", "J", "7"))]

        self.loop = [['.'] * len(self.input[0]) for _ in range(len(self.input))]

    def find_start_pos(self):
        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if self.input[y][x] == 'S':
                    return AT((x, y))

    def next_move(self, pos, dir_):
        move = self.input[pos[1]][pos[0]]
        if self.MOVE_MAP[move][0] == -dir_:
            next_dir = self.MOVE_MAP[move][1]
        else:
            next_dir = self.MOVE_MAP[move][0]
        return pos + next_dir, next_dir

    def find_first_move(self, pos):
        lines = relaxed_str_list(self.input)
        possible_moves = []
        for dir_ in self.DIR_MAP.values():
            next_pos = pos + dir_
            move = lines[next_pos[1]][next_pos[0]]
            if move not in self.MOVE_MAP:
                continue
            if -dir_ in self.MOVE_MAP[move]:
                possible_moves.append(dir_)
        assert (len(possible_moves) == 2)
        for k, v in self.MOVE_MAP.items():
            if set(v) == set(possible_moves):
                self.loop[pos[1]][pos[0]] = k
        return pos + possible_moves[0], possible_moves[0]

    def count_inside(self):
        class State(Enum):
            Out = auto()
            In = auto()
            EnterHorFromTop = auto()
            EnterHorFromBottom = auto()
            LeaveHorFromTop = auto()
            LeaveHorFromBottom = auto()

        total = 0
        for line in self.loop:
            state = State.Out
            for c in line:
                match state, c:
                    case State.Out, '|':
                        state = State.In
                    case State.Out, 'F':
                        state = State.EnterHorFromBottom
                    case State.Out, 'L':
                        state = State.EnterHorFromTop
                    case State.In, '.':
                        total += 1
                    case State.In, '|':
                        state = State.Out
                    case State.In, 'F':
                        state = State.LeaveHorFromBottom
                    case State.In, 'L':
                        state = State.LeaveHorFromTop
                    case State.EnterHorFromTop, '7':
                        state = State.In
                    case State.EnterHorFromTop, 'J':
                        state = State.Out
                    case State.EnterHorFromBottom, '7':
                        state = State.Out
                    case State.EnterHorFromBottom, 'J':
                        state = State.In
                    case State.LeaveHorFromTop, '7':
                        state = State.Out
                    case State.LeaveHorFromTop, 'J':
                        state = State.In
                    case State.LeaveHorFromBottom, '7':
                        state = State.In
                    case State.LeaveHorFromBottom, 'J':
                        state = State.Out
        return total

    @answer((6800, 483))
    def solve(self) -> tuple[int, int]:
        self.init()
        start_pos = self.find_start_pos()
        pos, dir_ = self.find_first_move(start_pos)
        i = 1
        while True:
            self.loop[pos[1]][pos[0]] = self.input[pos[1]][pos[0]]
            pos, dir_ = self.next_move(pos, dir_)
            i += 1
            if pos == start_pos:
                break
        return i // 2, self.count_inside()
