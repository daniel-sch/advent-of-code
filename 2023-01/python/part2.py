import re

NUMBERS = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine"]
FIRST_NUMBER_REGEX = re.compile("(" + "|".join(NUMBERS) + ")")
LAST_NUMBER_REGEX = re.compile("(?s:.*)(" + "|".join(NUMBERS) + ")")


def run(filename):
    f = open(filename, "r")
    result = 0
    while line := f.readline():
        first_number = FIRST_NUMBER_REGEX.search(line).group(1)
        last_number = LAST_NUMBER_REGEX.search(line).group(1)
        result += NUMBERS.index(first_number) % 10 * 10 + NUMBERS.index(last_number) % 10
    return result


if __name__ == "__main__":
    print(run("../input.txt"))
