import re
from collections import defaultdict
from operator import itemgetter

from .itertools import partition


def solve(file):
    grid_claims = defaultdict(list)

    re_claim = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    for line in filter(None, file):
        match = re_claim.match(line)
        claim, left, top, width, height = map(int, match.groups())

        for x in range(left, left + width):
            for y in range(top, top + height):
                grid_claims[(x, y)].append(claim)

    only_one, two_or_more = partition(lambda c: len(c) > 1, grid_claims.values())
    only_one = set(map(itemgetter(0), only_one))
    two_or_more = list(two_or_more)

    print('Part 1:', len(two_or_more))

    for claims in two_or_more:
        for claim in claims:
            if claim in only_one:
                only_one.remove(claim)

    assert len(only_one) == 1
    print('Part 2:', only_one.pop())
