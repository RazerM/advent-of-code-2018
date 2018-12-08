from .itertools import take


def sum_metadata(numbers):
    numbers = iter(numbers)
    value = 0

    while True:
        num_children = next(numbers)
        num_metadata = next(numbers)

        value += sum(sum_metadata(numbers) for _ in range(num_children))
        value += sum(take(num_metadata, numbers))

        break

    return value


def node_value(numbers):
    numbers = iter(numbers)
    value = 0

    while True:
        num_children = next(numbers)
        num_metadata = next(numbers)

        children = [node_value(numbers) for _ in range(num_children)]

        for metadata in take(num_metadata, numbers):
            if num_children:
                try:
                    value += children[metadata - 1]
                except IndexError:
                    pass
            else:
                value += metadata

        break

    return value


def solve(file):
    numbers = [int(x) for x in file.read().split()]

    metadata = sum_metadata(numbers)
    print('Part 1:', metadata)

    metadata = node_value(numbers)
    print('Part 2:', metadata)
