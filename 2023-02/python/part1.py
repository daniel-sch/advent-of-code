import re

MAX_CUBES = dict(red=12, green=13, blue=14)
CUBE_REGEX = re.compile(r"(\d+) (\w+)")


def is_game_possible(game_string):
    return all((MAX_CUBES[c] >= int(n) for n, c in CUBE_REGEX.findall(game_string)))


if __name__ == "__main__":
    print(sum((i for i, line in enumerate(open("../input.txt", "r").readlines(), 1) if is_game_possible(line))))
