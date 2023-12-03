def run(file):
    result = 0
    while line := file.readline():
        numbers = [int(c) for c in line if c.isdigit()]
        result += numbers[0] * 10 + numbers[-1]
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
