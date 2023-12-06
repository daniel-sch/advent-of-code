import math


def run(file):
    times = map(int, file.readline().split(':')[1].split())
    distances = map(int, file.readline().split(':')[1].split())
    result = 1
    for t, d in zip(times, distances):
        # Find roots of polynomial x*(t-x)-(d+1) = -x^2+tx-(d+1)
        p = -t
        q = d + 1
        x1 = (-p - math.sqrt(p ** 2 - 4 * q)) / 2
        x2 = (-p + math.sqrt(p ** 2 - 4 * q)) / 2
        result *= math.floor(x2) - math.ceil(x1) + 1
    return int(result)


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
