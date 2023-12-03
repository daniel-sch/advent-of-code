import re

NUMBER_REGEX = re.compile(r"(\d+)")
STAR_REGEX = re.compile(r"\*")


def get_range(vec, imin, imax, inclusive=False):
    return vec[max(0, imin): min(len(vec) - 1, imax) + 1 if inclusive else min(len(vec), imax)]


def adjacent_numbers(lines, line_idx, col_idx):
    return sum(
        ([int(c.group()) for c in NUMBER_REGEX.finditer(line) if c.start() - 1 <= col_idx < c.end() + 1]
         for line in get_range(lines, line_idx - 1, line_idx + 1, inclusive=True)), [])


def run(file):
    lines = file.readlines()
    result = 0
    for i, line in enumerate(lines):
        for c in STAR_REGEX.finditer(line):
            numbers = adjacent_numbers(lines, i, c.start())
            if len(numbers) == 2:
                result += numbers[0] * numbers[1]
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
