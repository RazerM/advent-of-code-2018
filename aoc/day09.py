import re

from collections import deque


re_input = re.compile(r'(\d+) players; last marble is worth (\d+) points')


def calculate_max_score(players, last_marble):
    marbles = deque([0])
    marble = 1
    player = 0

    # we use 0-indexed players in contrast to the question using 1-indexed
    player_scores = [0] * players

    while marble <= last_marble:
        if marble % 23 == 0:
            marbles.rotate(7)
            player_scores[player] += marble + marbles.popleft()
        else:
            marbles.rotate(-2)
            marbles.appendleft(marble)
        marble += 1
        player += 1
        player %= players

    return max(player_scores)


def solve(file, verbose):
    players, last_marble = map(int, re_input.match(file.read()).groups())

    print('Part 1:', calculate_max_score(players, last_marble))
    print('Part 2:', calculate_max_score(players, last_marble * 100))
