import pytest

from aoc.day01 import final_frequency, first_repeated_frequency


@pytest.mark.parametrize('changes, frequency', [
    ([1, -2, 3, 1], 3),
    ([1, 1, 1], 3),
    ([-1, -2, -3], -6),
])
def test_final_frequence(changes, frequency):
    assert final_frequency(changes) == frequency


@pytest.mark.parametrize('changes, frequency', [
    ([1, -2, 3, 1], 2),
    ([1, -1], 0),
    ([3, 3, 4, -2, -4], 10),
    ([-6, 3, 8, 5, -6], 5),
    ([7, 7, -2, -7, -4], 14)
])
def test_first_repeated_frequency(changes, frequency):
    assert first_repeated_frequency(changes) == frequency
