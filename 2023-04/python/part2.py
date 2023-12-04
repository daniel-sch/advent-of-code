import re

LINE_REGEX = re.compile(r".*: (.*) \| (.*)")


def run(file):
    card_wins = []
    while line := file.readline():
        m = LINE_REGEX.match(line)
        winning_numbers = {int(x) for x in m.group(1).split()}
        own_numbers = {int(x) for x in m.group(2).split()}
        card_wins.append(len(winning_numbers & own_numbers))
    card_count = [1] * len(card_wins)
    for i, card_win in enumerate(card_wins):
        for j in range(min(i + 1, len(card_wins)), min(card_win + i, len(card_wins)) + 1):
            card_count[j] += card_count[i]
    return sum(card_count)


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
