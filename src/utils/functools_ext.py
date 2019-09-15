def reduce_right(function, iterable, initializer=None):
    it = reversed(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


def find_n_builder(n: int = -1):
    def find(iterable, predicate):

        match = predicate if callable(predicate) else lambda f: f == predicate
        matches = []
        it = iter(iterable)

        for element in it:
            if match(element):
                matches.append(element)
                if len(matches) == n:
                    return matches if n > 1 else matches[0]
        else:
            return matches if len(matches) > 1 else None

    return find


find = find_n_builder(1)
find_all = find_n_builder(-1)


def identity(n):
    return n


def uniq(iter):
    return list(set(iter))


def compose(*functions):
    return reduce_right(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


if __name__ == '__main__':
    fn = compose(int, lambda n: n*10, str)

    print(fn('12'))
