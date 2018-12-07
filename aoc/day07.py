import copy
import re
from collections import defaultdict
from itertools import chain

from sortedcontainers import SortedSet

re_instruction = re.compile(
    r'Step (\w) must be finished before step (\w) can begin.')


def calculate_step_order(deps, num_workers=1, duration=lambda _: 0):
    deps = copy.deepcopy(deps)
    order = []

    # find steps without any dependencies
    nodes_without_dependencies = SortedSet(chain.from_iterable(deps.values()))
    nodes_without_dependencies -= deps.keys()

    t = 0
    blocked_until = dict()

    workers = [None] * num_workers
    worker_blocked_until = dict()

    while nodes_without_dependencies or worker_blocked_until:
        # use list so we can mutate dict
        for worker_idx, unblock_time in list(worker_blocked_until.items()):
            if unblock_time <= t:
                order.append(workers[worker_idx])
                workers[worker_idx] = None
                del worker_blocked_until[worker_idx]

        for worker_idx, work in enumerate(workers):
            if work:
                # This worker is busy
                continue

            for candidate in nodes_without_dependencies:
                if blocked_until.get(candidate, 0) <= t:
                    step = candidate
                    step_duration = duration(step)
                    workers[worker_idx] = step
                    nodes_without_dependencies.remove(step)
                    worker_blocked_until[worker_idx] = t + step_duration
                    break
            else:
                # Nothing for this worker to do
                continue

            for next_step, next_step_dependencies in deps.items():
                if step not in next_step_dependencies:
                    continue

                next_step_dependencies.remove(step)

                if not next_step_dependencies:
                    blocked_until[next_step] = t + step_duration
                    nodes_without_dependencies.add(next_step)

        t += 1

    return ''.join(order), t - 1


def make_duration_fn(*, delay=60):
    def duration(step):
        return delay + ord(step) - ord('A') + 1
    return duration


def parse_dependencies(lines):
    deps = defaultdict(SortedSet)

    for line in lines:
        match = re_instruction.match(line)
        step, prerequisite = match.groups()
        deps[prerequisite].add(step)

    return deps


def solve(file):
    deps = parse_dependencies(file)

    order, _ = calculate_step_order(deps)
    print('Part 1:', order)

    duration = make_duration_fn()
    _, time = calculate_step_order(deps, num_workers=5, duration=duration)
    print('Part 2:', time)
