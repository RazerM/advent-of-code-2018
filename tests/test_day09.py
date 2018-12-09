import pytest

from aoc.day09 import calculate_max_score


@pytest.mark.parametrize('players, last_marble, score', [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
])
def test_max_score(players, last_marble, score):
    assert calculate_max_score(players, last_marble) == score
