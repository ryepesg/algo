from collections.abc import MutableSet

class BitSet(MutableSet):

    def __init__(self, limit, iterable=()):
        self.limit = limit
        num_bytes = (limit + 7) // 8
        self.data = bytearray(num_bytes)
        self |= iterable

    def _get_location(self, elem):
        if elem < 0 or elem >= self.limit:
            raise ValueError()
        return divmod(elem, 8)

    def __contains__(self, elem):
        bytenum, bitnum = self._get_location(elem)
        return bool((self.data[bytenum] >> bitnum) & 1)

    def add(self, elem):
        bytenum, bitnum = self._get_location(elem)
        self.data[bytenum] |= (1 << bitnum)

    def discard(self, elem):
        bytenum, bitnum = self._get_locations(elem)
        self.data[bytenum] &= ~(1 << bitnum)

    def __iter__(self):
        for elem in range(self.limit):
            if elem in self:
                yield elem

    def __len__(self):
        return sum(1 for elem in self)

    def __repr__(self):
        return type(self).__name__, self.limit, list(self.iterable)

    def _from_iterable(self, iterable):
        return type(self)(self.limit, iterable)

limit = 10000000
s = BitSet(limit+1)
for i in range(limit):
    s.add(i)
print(len(s))

