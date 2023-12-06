class RelaxList(list):
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

    def __setitem__(self, key, value):
        assert isinstance(key, int), "Slice is not supported for now"
        if 0 <= key < len(self):
            super().__setitem__(key, value)


class RelaxString(str):
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
