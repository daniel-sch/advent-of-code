def run(filename):
    f = open(filename, "r")
    line = f.readline()
    floor = 0
    for pos, char in enumerate(line, 1):
        floor += 1 if char == "(" else -1
        if floor == -1:
            return pos


if __name__ == "__main__":
    print(run("../input.txt"))
