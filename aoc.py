#!/usr/bin/env python3
import click
import aoc

SOLVERS = {
    1: aoc.day1.solve,
}


@click.command()
@click.argument('day', type=click.IntRange(min=1, max=25))
@click.argument('file', type=click.File('r'), default='-')
def cli(day, file):
    """If FILE is not passed, stdin is used instead."""
    try:
        solve = SOLVERS[day]
    except KeyError:
        click.echo('Unimplemented!', err=True)
        raise click.Abort

    solve(file)


if __name__ == '__main__':
    cli()
