def consolidate_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][0] + ranges[i][1] >= ranges[i + 1][0]:
            range_i_stop = ranges[i][0] + ranges[i][1]
            range_i1_stop = ranges[i + 1][0] + ranges[i + 1][1]
            ranges[i] = (ranges[i][0], max(range_i_stop, range_i1_stop) - ranges[i][0])
            del ranges[i + 1]
        else:
            i += 1
    return ranges


def map_range(range_, mapping):
    range_start, range_stop = range_[0], range_[0] + range_[1]
    mapping_start, mapping_stop, mapping_delta = mapping[1], mapping[1] + mapping[2], mapping[0] - mapping[1]

    leftover_ranges = []
    mapped_range = []
    if range_start < mapping_start:  # part of range that is left of mapping
        start = range_start
        leftover_ranges.append((start, min(range_stop, mapping_start) - start))
    if max(range_start, mapping_start) < min(range_stop, mapping_stop):  # overlapping part will be mapped
        start = max(range_start, mapping_start)
        stop = min(range_stop, mapping_stop)
        mapped_range.append((start + mapping_delta, stop - start))
    if range_stop > mapping_stop:  # part of range that is right of mapping
        start = max(mapping_stop, range_start)
        leftover_ranges.append((start, range_stop - start))
    return leftover_ranges, mapped_range


def run(file):
    seeds = [int(x) for x in file.readline().split(": ")[1].split()]
    leftover_ranges = list(zip(seeds[::2], seeds[1::2]))
    mapped_ranges = []
    while line := file.readline():
        if len(line) == 1:  # new map starts
            leftover_ranges = consolidate_ranges(leftover_ranges + mapped_ranges)
            print(len(leftover_ranges))
            mapped_ranges = []
        elif line[0].isdigit():  # new line for map
            mapping = [int(x) for x in line.split()]
            temp_ranges = []
            for r in leftover_ranges:
                l, m = map_range(r, mapping)
                temp_ranges += l
                mapped_ranges += m
            leftover_ranges = temp_ranges
    return min((x[0] for x in leftover_ranges + mapped_ranges))


if __name__ == "__main__":
    with open("../input.txt", 'r') as f:
        print(run(f))
