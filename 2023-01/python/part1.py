def run(filename):
    f = open(filename, "r")
    result = 0
    while line := f.readline():
        numbers = [int(c) for c in line if c.isdigit()]
        result += numbers[0] * 10 + numbers[-1]
    return result


if __name__ == "__main__":
    print(run("../input.txt"))
