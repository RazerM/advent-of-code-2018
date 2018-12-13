def should_destroy(a, b):
    return (
        (a.isupper() and b.islower() and a.lower() == b) or
        (b.isupper() and a.islower() and b.lower() == a)
    )


def react_polymer(poly_chain):
    # make a copy, also covers str -> list
    poly_chain = list(poly_chain)

    i = 1
    while i < len(poly_chain):
        x = poly_chain[i - 1]
        y = poly_chain[i]

        if should_destroy(x, y):
            # delete x
            del poly_chain[i - 1]
            i -= 1

            # delete y
            del poly_chain[i]
        else:
            i += 1

    return poly_chain


def remove_polymer(poly_chain, polymer):
    return [c for c in poly_chain if c.lower() != polymer]


def remove_problem_polymer(poly_chain):
    candidates = set(p for p in poly_chain if p.islower())
    return min(
        (react_polymer(remove_polymer(poly_chain, p)) for p in candidates),
        key=len,
    )


def solve(file, verbose):
    poly_chain = file.read().strip()
    print('Part 1:', len(react_polymer(poly_chain)))
    print('Part 2:', len(remove_problem_polymer(poly_chain)))
