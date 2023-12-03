def run(file):
    line = file.readline()
    floor = 0
    for pos, char in enumerate(line, 1):
        floor += 1 if char == "(" else -1
        if floor == -1:
            return pos


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
