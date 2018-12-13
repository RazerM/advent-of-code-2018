from .itertools import take


def sum_metadata(numbers):
    numbers = iter(numbers)

    num_children = next(numbers)
    num_metadata = next(numbers)

    return (
        sum(sum_metadata(numbers) for _ in range(num_children)) +
        sum(take(num_metadata, numbers))
    )


def node_value(numbers):
    numbers = iter(numbers)

    num_children = next(numbers)
    num_metadata = next(numbers)

    children = [node_value(numbers) for _ in range(num_children)]
    metadata = take(num_metadata, numbers)

    if num_children:
        return sum(children[m - 1] for m in metadata if m - 1 < len(children))

    return sum(metadata)


def solve(file, verbose):
    numbers = [int(x) for x in file.read().split()]

    metadata = sum_metadata(numbers)
    print('Part 1:', metadata)

    value = node_value(numbers)
    print('Part 2:', value)
