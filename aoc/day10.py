import re
from itertools import count

import attr

from .itertools import minmax, peak_to_peak

re_pos_vel = re.compile(
    r'position=<(\s*-?\d+),(\s*-?\d+)> velocity=<(\s*-?\d+),(\s*-?\d+)>')


@attr.s
class Vector:
    x = attr.ib()
    y = attr.ib()

    def as_tuple(self):
        return self.x, self.y

    # we only use +=, so I didn't add the others

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
            self.x += x
            self.y += y
            return self
        return NotImplemented


@attr.s
class Point:
    pos = attr.ib(converter=lambda p: Vector(*p))
    vel = attr.ib(converter=lambda v: Vector(*v))


LETTERS = {
    287404110897234175: 'A',
    574773553322788098: 'C',
    1151796705286423553: 'L',
    1152217920269458431: 'N',
    1152394323728839107: 'R',
    584915465790883713: 'Z',
}


def parse_message(points):
    min_y, max_y = minmax(p.pos.y for p in points)
    min_x, max_x = minmax(p.pos.x for p in points)

    grid = dict()

    for point in points:
        grid[point.pos.as_tuple()] = '1'

    character = []

    message = ''

    def append_character():
        nonlocal character
        nonlocal message
        char_int = int(''.join(character), 2)

        try:
            message += LETTERS[char_int]
        except KeyError:
            message += '?'
            print(f'Unknown letter for {char_int}, please add to LETTERS:')
            s = ''.join('#' if c == '1' else ' ' for c in character)
            lines = [s[i:i+10] for i in range(0, len(s), 10)]

            rows = []
            for i in range(len(lines[0])):
                row = [line[i] for line in lines]
                rows.append(''.join(row))

            print('\n'.join(rows))
        character = []

    for x in range(min_x, max_x + 1):
        column = []
        for y in range(min_y, max_y + 1):
            column.append(grid.get((x, y), '0'))

        if all(c == '0' for c in column):
            if character:
                append_character()
        else:
            character.extend(column)

    # append the last character
    append_character()

    return message


def find_message(points):
    for t in count():
        y_range = peak_to_peak(p.pos.y for p in points)

        if y_range < 10:
            message = parse_message(points)
            break

        for point in points:
            point.pos += point.vel

    return message, t


def solve(file):
    points = []
    for line in file:
        px, py, vx, vy = map(int, re_pos_vel.match(line).groups())
        points.append(Point(pos=(px, py), vel=(vx, vy)))

    message, seconds = find_message(points)

    print('Part 1:', message)
    print('Part 2:', seconds)
