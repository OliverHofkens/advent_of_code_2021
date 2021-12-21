#!/usr/bin/env python

import sys
from itertools import count, cycle
from typing import Iterator


def deterministic_dice_rolls() -> Iterator[int]:
    _sum = 0
    _count = 0
    for roll in count(1):
        _sum += roll
        _count += 1
        if _count % 3 == 0:
            yield _sum
            _sum = 0


def main():
    player_pos = [int(line.strip().split(": ")[1]) for line in sys.stdin.readlines()]
    player_score = [0, 0]

    for n_turns, (player, roll) in enumerate(
        zip(cycle((0, 1)), deterministic_dice_rolls()), 1
    ):
        player_pos[player] += roll
        player_pos[player] = (player_pos[player] % 10) or 10
        player_score[player] += player_pos[player]

        if player_score[player] >= 1000:
            n_rolls = n_turns * 3
            lowest_score = min(player_score)
            print(n_rolls * lowest_score)
            break


if __name__ == "__main__":
    main()
