from aoc.day07 import calculate_step_order, make_duration_fn, parse_dependencies

example = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".lstrip()


def test_part1_example():
    deps = parse_dependencies(example.splitlines())
    order, _ = calculate_step_order(deps)
    assert order == 'CABDFE'


def test_part2_example():
    deps = parse_dependencies(example.splitlines())
    duration = make_duration_fn(delay=0)
    order, time = calculate_step_order(deps, num_workers=2, duration=duration)
    assert order == 'CABFDE'
    assert time == 15
