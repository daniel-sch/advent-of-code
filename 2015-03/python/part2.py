def process_santa(visited, instr):
    x, y = 0, 0
    for c in instr:
        match c:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        visited.add((x, y))


def run(file):
    line = file.readline()
    visited = {(0, 0)}
    process_santa(visited, line[::2])
    process_santa(visited, line[1::2])
    return len(visited)


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
