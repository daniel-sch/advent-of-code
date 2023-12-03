def run(file):
    line = file.readline()
    x, y = 0, 0
    visited = {(0, 0)}
    for c in line:
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
    return len(visited)


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
