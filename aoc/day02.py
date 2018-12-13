import operator
from collections import Counter
from itertools import combinations, starmap


def checksum(box_ids):
    twice = 0
    thrice = 0

    for box_id in box_ids:
        c = Counter(box_id)

        v = set(c.values())
        if 2 in v:
            twice += 1
        if 3 in v:
            thrice += 1

    return twice * thrice


def common_letters(box_ids):
    for id1, id2 in combinations(box_ids, 2):
        n = 0
        idx = None

        for i, different in enumerate(starmap(operator.ne, zip(id1, id2))):
            if different:
                n += 1
                idx = i

                # early break
                if n > 1:
                    break

        if n > 1:
            continue

        return id1[:idx] + id1[idx + 1:]


def solve(file, verbose):
    box_ids = [line.strip() for line in file]

    print('Part 1:', checksum(box_ids))
    print('Part 2:', common_letters(box_ids))
