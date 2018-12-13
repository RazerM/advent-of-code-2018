from collections import deque

from .itertools import range1


def get_plant(state, i):
    try:
        return state[i]
    except KeyError:
        return '.'


def calc_sum(state):
    return sum(k for k, v in state.items() if v == '#')


def sum_generations(state, patterns, generations):
    new_sum = old_sum = calc_sum(state)
    sum_diffs = deque(maxlen=3)

    for generation in range1(generations):
        imin = min(state)
        imax = max(state)

        state[imin - 1] = '.'
        state[imax + 1] = '.'

        new_state = dict()

        for i, c in state.items():
            l2 = get_plant(state, i - 2)
            l1 = get_plant(state, i - 1)
            r1 = get_plant(state, i + 1)
            r2 = get_plant(state, i + 2)

            new_state[i] = patterns.get((l2, l1, c, r1, r2), '.')

        state = new_state
        new_sum = calc_sum(state)
        sum_diffs.append(new_sum - old_sum)

        # shortcut if we find a repeating pattern
        if len(sum_diffs) > 1 and len(set(sum_diffs)) == 1:
            return (generations - generation) * sum_diffs[0] + new_sum

        old_sum = new_sum

    return new_sum


def solve(file, verbose):
    patterns = dict()
    state = None
    for i, line in enumerate(file):
        if i == 0:
            _, _, initial = line.partition('initial state: ')
            state = dict(enumerate(initial.strip()))

        if not line:
            continue

        pattern, _, output = line.partition(' => ')
        patterns[tuple(pattern)] = output.strip()

    print('Part 1:', sum_generations(state, patterns, 20))
    print('Part 2:', sum_generations(state, patterns, 50_000_000_000))
