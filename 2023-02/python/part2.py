import math
import re

CUBE_REGEX = re.compile(r"(\d+) (\w+)")


def fewest_cubes_prod(game_string):
    min_cubes = dict(red=0, green=0, blue=0)
    for amount, color in CUBE_REGEX.findall(game_string):
        min_cubes[color] = max(int(amount), min_cubes[color])
    return math.prod(min_cubes.values())


if __name__ == "__main__":
    print(sum((fewest_cubes_prod(line) for line in open("../input.txt", "r").readlines())))
