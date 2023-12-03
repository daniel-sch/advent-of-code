import re

FORBIDDEN_REGEX = re.compile(r"ab|cd|pq|xy")
VOWEL_REGEX = re.compile(r"[aeiou]")
DOUBLE_REGEX = re.compile(r"(.)\1")


def is_nice(line):
    return FORBIDDEN_REGEX.search(line) is None \
        and len(VOWEL_REGEX.findall(line)) >= 3 \
        and DOUBLE_REGEX.search(line) is not None


def run(file):
    return sum((is_nice(line) for line in file.readlines()))


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
