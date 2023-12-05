def run(file):
    seeds = [int(x) for x in file.readline().split(": ")[1].split()]
    new_seeds = seeds
    while line := file.readline():
        if len(line) == 1:  # new map starts
            seeds = new_seeds
            new_seeds = seeds.copy()
        elif line[0].isdigit():  # new line for map
            mapping = [int(x) for x in line.split()]
            for i, s in enumerate(seeds):
                if 0 <= s - mapping[1] < mapping[2]:
                    new_seeds[i] = s + mapping[0] - mapping[1]
    return min(new_seeds)


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
