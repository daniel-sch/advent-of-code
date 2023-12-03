import re

DOUBLE_REGEX = re.compile(r"(..).*\1")
REPEATS_REGEX = re.compile(r"(.).\1")


def is_nice(line):
    return DOUBLE_REGEX.search(line) is not None and REPEATS_REGEX.search(line) is not None


def run(file):
    return sum((is_nice(line) for line in file.readlines()))


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
