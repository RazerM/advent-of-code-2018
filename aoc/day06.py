from collections import defaultdict


def manhattan(m, n):
    return abs(m[0] - n[0]) + abs(m[1] - n[1])


def calculate_areas(coords, *, gap=0):
    max_x, max_y = map(max, zip(*coords))
    min_x, min_y = map(min, zip(*coords))

    coord_areas = defaultdict(list)

    for x in range(min_x - gap, max_x + gap + 1):
        for y in range(min_y - gap, max_y + gap + 1):
            shortest = defaultdict(list)
            for cx, cy in coords:
                m = manhattan((cx, cy), (x, y))
                shortest[m].append((cx, cy))
            closest_coords = shortest[min(shortest)]

            # exclude ties
            if len(closest_coords) > 1:
                continue

            coord_areas[closest_coords[0]].append((x, y))

    return {len(v) for v in coord_areas.values()}


def find_region_size(coords):
    in_region = 0

    max_x, max_y = map(max, zip(*coords))
    min_x, min_y = map(min, zip(*coords))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total = 0
            for cx, cy in coords:
                total += manhattan((cx, cy), (x, y))
            if total < 10000:
                in_region += 1

    return in_region


def solve(file):
    coords = []
    for line in file:
        x, y = map(int, line.split(','))
        coords.append((x, y))

    # The infinite areas will get bigger when the grid does
    area_sizes1 = calculate_areas(coords)
    area_sizes2 = calculate_areas(coords, gap=2)

    print('Part 1:', max(area_sizes1 & area_sizes2))
    print('Part 2:', find_region_size(coords))
