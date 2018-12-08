from itertools import chain, filterfalse, islice, tee


def first_repetition(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            return item
        seen.add(item)


def prepend(value, iterator):
    return chain([value], iterator)


def partition(pred, iterable):
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def take(n, iterable):
    return islice(iterable, n)
