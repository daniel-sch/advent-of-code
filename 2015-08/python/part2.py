def run(file):
    result = 0
    while line := file.readline():
        line = line.strip()
        line_escaped = repr(line.replace('"', "'") + '"')  # ugly hack to convince repr to escape the "
        result += len(line_escaped) - len(line) - 1
        print(f"{line} => {line_escaped}")
    return result


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
