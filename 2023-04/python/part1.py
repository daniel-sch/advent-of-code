import re

LINE_REGEX = re.compile(r".*: (.*) \| (.*)")


def run(file):
    result = 0
    while line := file.readline():
        m = LINE_REGEX.match(line)
        winning_numbers = {int(x) for x in m.group(1).split()}
        own_numbers = {int(x) for x in m.group(2).split()}
        intersect = len(winning_numbers & own_numbers)
        if intersect:
            result += 2 ** (intersect - 1)
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
