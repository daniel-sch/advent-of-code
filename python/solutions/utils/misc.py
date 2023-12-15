def index_iter(haystack, needles):
    for i, el in enumerate(haystack):
        if el in needles:
            yield i


def split(lst, separators, return_empty=True):
    g = []
    for el in lst:
        if el in separators:
            if len(g) > 0 or return_empty:
                yield g
                g = []
        else:
            g.append(el)
    if len(g) > 0 or return_empty:
        yield g


def split_lengths(lst, separators, return_empty=True):
    group_len = 0
    for el in lst:
        if el in separators:
            if group_len > 0 or return_empty:
                yield group_len
                group_len = 0
        else:
            group_len += 1
    if group_len > 0 or return_empty:
        yield group_len
