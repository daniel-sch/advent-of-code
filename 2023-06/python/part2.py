import math


def run(file):
    t = int(file.readline().split(':')[1].replace(' ', ''))
    d = int(file.readline().split(':')[1].replace(' ', ''))
    # Find roots of polynomial x*(t-x)-(d+1) = -x^2+tx-(d+1)
    p = -t
    q = d + 1
    x1 = (-p - math.sqrt(p ** 2 - 4 * q)) / 2
    x2 = (-p + math.sqrt(p ** 2 - 4 * q)) / 2
    return math.floor(x2) - math.ceil(x1) + 1


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
