def run(filename):
    f = open(filename, "r")
    line = f.readline()
    return line.count("(") - line.count(")")


if __name__ == "__main__":
    print(run("../input.txt"))
