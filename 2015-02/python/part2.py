def run(file):
    result = 0
    while line := file.readline():
        dims = sorted([int(x) for x in line.split('x')])
        result += 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2]
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
