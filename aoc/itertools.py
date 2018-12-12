from collections.abc import Iterator

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


def minmax(iterable):
    if isinstance(iterable, Iterator):
        iterable = list(iterable)
    return min(iterable), max(iterable)


def peak_to_peak(iterable):
    mn, mx = minmax(iterable)
    return mx - mn
