import re

import numpy as np

LINE_REGEX = re.compile(r"(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)")


def run(file):
    lights = np.zeros((1000, 1000), dtype=bool)
    while line := file.readline():
        m = LINE_REGEX.match(line)
        idx = np.s_[int(m.group(2)):int(m.group(4)) + 1, int(m.group(3)):int(m.group(5)) + 1]
        match m.group(1):
            case "turn on":
                lights[idx] = True
            case "turn off":
                lights[idx] = False
            case "toggle":
                lights[idx] = ~lights[idx]
    return np.sum(lights)


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
