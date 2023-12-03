from ast import literal_eval


def run(file):
    result = 0
    while line := file.readline():
        line = line.strip()
        line_eval = literal_eval(line)
        result += len(line) - len(line_eval)
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
