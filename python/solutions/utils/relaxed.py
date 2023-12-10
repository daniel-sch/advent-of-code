class RelaxList(list):
    """List class that returns a given default value for out-of-bounds reads and discards out-of-bounds writes."""

    def __init__(self, items, default_value=None):
        super().__init__(items)
        self.default_value = default_value

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = max(0, min(item.start, len(self)))
            stop = max(0, min(item.stop, len(self) + 1))
            assert item.step is None or item.step == 1, "Weird things will happen if step != 1"
            return super().__getitem__(slice(start, stop))
        else:
            if 0 <= item < len(self):
                return super().__getitem__(item)
            else:
                return self.default_value

    def __setitem__(self, key, value):
        assert isinstance(key, int), "Slice is not supported for now"
        if 0 <= key < len(self):
            super().__setitem__(key, value)


class RelaxString(str):
    """String class that returns None for out-of-bounds reads."""

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = max(0, min(item.start, len(self)))
            stop = max(0, min(item.stop, len(self) + 1))
            assert item.step is None or item.step == 1, "Weird things will happen if step != 1"
            return super().__getitem__(slice(start, stop))
        else:
            if 0 <= item < len(self):
                return super().__getitem__(item)
            else:
                return None


def relaxed_str_list(str_list):
    return RelaxList((RelaxString(x) for x in str_list), RelaxString(""))
