from operator import add, sub


class AT(tuple):
    """Tuple class, which can be added and subtracted from other tuples."""

    def __add__(self, other):
        if isinstance(other, tuple):
            assert len(self) == len(other)
            return AT(map(add, self, other))
        else:
            return AT(map(lambda x: x + other, self))

    def __sub__(self, other):
        if isinstance(other, tuple):
            assert len(self) == len(other)
            return AT(map(sub, self, other))
        else:
            return AT(map(lambda x: x - other, self))

    def __neg__(self):
        return AT(map(lambda x: -x, self))
