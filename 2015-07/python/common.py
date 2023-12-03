import re

LINE_REGEX = re.compile(r"(\w+)?? ?([A-Z]+)? ?(\w+) -> ([a-z]+)")
UNARY_OPERATORS = [None, "NOT"]


def parse_value(signals, in_):
    if in_:
        if in_.isdigit():
            return int(in_)
        elif in_ in signals:
            return signals[in_]
    return None


def compute_gate(op, first, second):
    match op:
        case None:
            return second
        case "NOT":
            return ~second
        case "AND":
            return first & second
        case "OR":
            return first | second
        case "LSHIFT":
            return first << second
        case "RSHIFT":
            return first >> second
        case _:
            assert False, f"Unknown op {op}"


def to_uint16(x):
    return x & 0xFFFF


def compute_all(lines, signals):
    while len(lines):
        new_lines = []
        for line in lines:
            m = LINE_REGEX.match(line)
            if m.group(4) in signals:
                continue
            first_value = parse_value(signals, m.group(1))
            second_value = parse_value(signals, m.group(3))
            if (m.group(2) not in UNARY_OPERATORS and first_value is None) or second_value is None:
                new_lines.append(line)
            else:
                signals[m.group(4)] = to_uint16(compute_gate(m.group(2), first_value, second_value))
        lines = new_lines
    return signals
