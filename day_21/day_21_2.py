#!/usr/bin/env python

import sys
from collections import Counter
from functools import cache
from itertools import product
from typing import Sequence, Tuple

# (pos_1, pos_2, score_1, score_2)
State = Tuple[int, int, int, int]

dice_roller = product((1, 2, 3), repeat=3)
roll_sum_count = Counter(sum(roll) for roll in dice_roller)


@cache
def play_game(state: State) -> Sequence[int]:
    """
    Returns:
        The win counts (w1, w2)
    """
    wins = [0, 0]

    for move, roll_count in roll_sum_count.items():
        # We play the current player's turn first:
        pos = state[0] + move
        pos = (pos % 10) or 10
        score = state[2] + pos

        # If this is a win, shortcut:
        if score >= 21:
            wins[0] += roll_count

        # Otherwise, play the next turn:
        else:
            # Swap all variables to represent the other player.
            p2_subwins, p1_subwins = play_game((state[1], pos, state[3], score))
            wins[0] += p1_subwins * roll_count
            wins[1] += p2_subwins * roll_count

    return wins


def main():
    player_pos = [int(line.strip().split(": ")[1]) for line in sys.stdin.readlines()]

    starting_state: State = (*player_pos, 0, 0)
    wins = play_game(starting_state)
    print(max(wins))


if __name__ == "__main__":
    main()
