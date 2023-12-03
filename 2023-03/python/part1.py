import re

NUMBER_REGEX = re.compile(r"(\d+)")
SYMBOL_REGEX = re.compile(r"[^\d\.\s]")


def get_range(vec, imin, imax, inclusive=False):
    return vec[max(0, imin): min(len(vec) - 1, imax) + 1 if inclusive else min(len(vec), imax)]


def is_symbol_adjacent(lines, line_idx, span):
    return any(map(lambda line: SYMBOL_REGEX.search(get_range(line, span[0] - 1, span[1] + 1)),
                   get_range(lines, line_idx - 1, line_idx + 1, inclusive=True)))


def run(file):
    lines = file.readlines()
    result = 0
    for i, line in enumerate(lines):
        for c in NUMBER_REGEX.finditer(line):
            if is_symbol_adjacent(lines, i, c.span()):
                result += int(c.group())
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
