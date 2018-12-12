from collections import deque, namedtuple

Place = namedtuple('Place', 'x y size')


def itemkey(item):
    return item[0]


def itemvalue(item):
    return item[1]


def calculate_power(x, y, serial_number):
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    power = int(abs(power / 100 % 10))
    power -= 5
    return power


def range1(*args):
    if len(args) == 1:
        return range(1, args[0] + 1)
    elif len(args) == 2:
        return range(args[0], args[1] + 1)
    elif len(args) == 3:
        return range(args[0], args[1] + 1, args[2])
    raise TypeError('Expected 1-3 args')


def solve(file):
    serial_number = int(file.read())

    grid_size = 300

    power_levels = {
        (0, 0): 0,
    }
    for n in range1(grid_size):
        power_levels[(n, 0)] = 0
        power_levels[(0, n)] = 0

    # https://en.wikipedia.org/wiki/Summed-area_table
    for x in range1(grid_size):
        for y in range1(grid_size):
            key = x, y
            power_level = calculate_power(x, y, serial_number)
            a = power_levels[(x, y - 1)]
            b = power_levels[(x - 1, y)]
            c = power_levels[(x - 1, y - 1)]

            power_levels[key] = power_level + a + b - c

    p = power_levels
    total_powers = dict()
    last_powers = deque(maxlen=3)

    for square_size in range1(grid_size):
        for x in range1(grid_size - square_size + 1):
            for y in range1(grid_size - square_size + 1):
                k = square_size - 1
                a = (x - 1, y - 1)
                b = (x + k, y - 1)
                c = (x - 1, y + k)
                d = (x + k, y + k)

                total_power = p[d] + p[a] - p[b] - p[c]
                total_powers[Place(x, y, square_size)] = total_power

        # Exit early by assuming convergence when sum hasn't changed in several
        # iterations
        last_powers.append(itemvalue(max(total_powers.items(), key=itemvalue)))
        if len(last_powers) > 1 and len(set(last_powers)) == 1:
            break

    size3_items = (x for x in total_powers.items() if itemkey(x).size == 3)
    part1 = itemkey(max(size3_items, key=itemvalue))
    part2 = itemkey(max(total_powers.items(), key=itemvalue))
    print('Part 1:', ','.join(map(str, part1[:2])))
    print('Part 2:', ','.join(map(str, part2)))
