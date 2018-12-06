from itertools import accumulate, cycle

from .itertools import first_repetition, prepend


def final_frequency(changes):
    return sum(changes)


def first_repeated_frequency(changes):
    return first_repetition(prepend(0, accumulate(cycle(changes))))


def solve(file):
    changes = [int(line) for line in file]

    print('Part 1:', final_frequency(changes))
    print('Part 2:', first_repeated_frequency(changes))
