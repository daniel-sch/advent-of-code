from common import compute_all


def run(file):
    lines = file.readlines()
    signals = compute_all(lines, dict())
    signals = compute_all(lines, dict(b=signals['a']))
    return signals['a']


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
