class Set:
    _n = 0
    _number_unions = 0

    def __init__(self):
        self.parent = self
        self.rank = 0
        self._inc_groups()

    @classmethod
    def _inc_groups(cls):
        cls._n += 1


def find(x):
    # this is used exclusively to find if 2 objects belong to the same set
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def _link(x, y):
    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        if x.rank == y:
            x.rank += 1


def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        Set._number_unions += 1
        _link(find(x), find(y))


def groups():
    return Set._n - Set._number_unions
