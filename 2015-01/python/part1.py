def run(file):
    line = file.readline()
    return line.count("(") - line.count(")")


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
