from itertools import chain


def first_repetition(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            return item
        seen.add(item)


def prepend(value, iterator):
    return chain([value], iterator)
