from enum import IntEnum

import attr

CART_DIRS = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0),
}

DIR_CARTS = {v: k for k, v in CART_DIRS.items()}

CART_TRACKS = {
    '^': '|',
    'v': '|',
    '<': '-',
    '>': '-',
}


class IntersectionTurn(IntEnum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2

    def cycle(self):
        return IntersectionTurn((self.value + 1) % 3)


@attr.s
class Cart:
    pos = attr.ib()
    direction = attr.ib()
    intersection_turn = attr.ib(default=IntersectionTurn.LEFT)

    def turn_left(self):
        x, y = self.direction
        self.direction = y, -x

    def turn_right(self):
        x, y = self.direction
        self.direction = -y, x


def cart_sort(cart):
    return cart.pos[1], cart.pos[0]


def solve(file, verbose: int):
    lines = [line.rstrip() for line in file]
    width = max(len(line) for line in lines)
    height = len(lines)

    lines = [line.ljust(width) for line in lines]
    grid = [[line[x] for line in lines] for x in range(width)]

    carts = []

    # move top to bottom, left to right for initial cart order
    for y in range(height):
        for x in range(width):
            current = grid[x][y]
            if current in CART_DIRS:
                carts.append(Cart(pos=(x, y), direction=CART_DIRS[current]))
                # put the underlying track piece there
                grid[x][y] = CART_TRACKS[current]

    first_crash = None
    last_pos = None
    while not first_crash or not last_pos:
        if verbose > 0:
            for y in range(height):
                for x in range(width):
                    for cart in carts:
                        if cart.pos == (x, y):
                            print(DIR_CARTS[cart.direction], end='')
                            break
                    else:
                        print(grid[x][y], end='')
                print()
            print()

        for cart in carts:
            x, y = cart.pos
            dx, dy = cart.direction
            horizontal = dx != 0

            x += dx
            y += dy
            cart.pos = x, y

            next_track = grid[x][y]
            if next_track in {'-', '|'}:
                pass
            elif next_track == '/':
                if horizontal:
                    cart.turn_left()
                else:
                    cart.turn_right()
            elif next_track == '\\':
                if horizontal:
                    cart.turn_right()
                else:
                    cart.turn_left()
            elif next_track == '+':
                if cart.intersection_turn is IntersectionTurn.LEFT:
                    cart.turn_left()
                elif cart.intersection_turn is IntersectionTurn.RIGHT:
                    cart.turn_right()
                cart.intersection_turn = cart.intersection_turn.cycle()
            else:
                raise RuntimeError(next_track)

            if len(carts) == 1:
                last_pos = cart.pos
                break

            if any(c for c in carts if c.pos == cart.pos and c is not cart):
                if first_crash is None:
                    first_crash = cart.pos
                # Remove crashed carts
                carts = [c for c in carts if c.pos != cart.pos]

        carts.sort(key=cart_sort)

    print('Part 1:', ','.join(map(str, first_crash)))
    print('Part 2:', ','.join(map(str, last_pos)))
