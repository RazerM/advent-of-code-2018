from tqdm import tqdm


def solve(file, verbose):
    num_recipes = int(file.read())
    find_seq = list(map(int, str(num_recipes)))

    elfs = [0, 1]
    recipes = [3, 7]

    part1 = None
    part2 = None

    tbar = tqdm(
        desc='Searching for part 1',
        disable=verbose < 1,
    )

    with tbar as bar:
        i = 0
        while part1 is None or part2 is None:
            bar.update(1)
            i += 1
            if verbose > 2:
                print(recipes)

            new_recipes = sum(recipes[i] for i in elfs)
            if new_recipes < 10:
                recipes.append(new_recipes)
            else:
                recipes.extend(divmod(new_recipes, 10))

            for elf, recipe in enumerate(elfs):
                elfs[elf] = (recipe + recipes[recipe] + 1) % len(recipes)

            if part1 is None and len(recipes) >= num_recipes + 10:
                part1 = ''.join(map(str, recipes[num_recipes:num_recipes + 10]))
                bar.write(f'Part 1: {part1}')
                if verbose > 0:
                    bar.set_description('Searching for part 2')

            if part2 is None:
                if recipes[-len(find_seq):] == find_seq:
                    part2 = len(recipes) - len(find_seq)
                elif recipes[-len(find_seq) - 1:-1] == find_seq:
                    part2 = len(recipes) - len(find_seq) - 1

    print('Part 2:', part2)
