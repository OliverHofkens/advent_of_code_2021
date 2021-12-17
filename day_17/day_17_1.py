#!/usr/bin/env python

import sys
from typing import Tuple

Vec2 = Tuple[int, int]


def trace_probe(velocity: Vec2, target_x: Vec2, target_y: Vec2) -> int:
    """
    Simulates the trajectory of the probe.
    Returns:
        None if the probe never reached the target,
        otherwise the max y reached.
    """
    pos = [0, 0]
    max_y = 0
    drag = -1 if velocity[0] > 0 else 1

    while True:
        pos[0] += velocity[0]
        pos[1] += velocity[1]
        velocity = velocity[0] + drag if velocity[0] != 0 else 0, velocity[1] - 1

        # Check if we missed the target:
        if pos[1] < target_y[0]:
            return 0

        if pos[1] > max_y:
            max_y = pos[1]

        # Check if we're in the target zone:
        if target_x[0] <= pos[0] <= target_x[1] and (
            target_y[0] <= pos[1] <= target_y[1]
        ):
            return max_y


def parse_target(inp: str) -> tuple:
    inp = inp[len("target area: ") :]
    parts = [map(int, p[2:].split("..")) for p in inp.split(", ")]
    return tuple(tuple(t) for t in parts)


def main():
    target_x, target_y = parse_target(sys.stdin.readline())

    # Ensure we shoot in the right direction:
    guess_x = range(0, target_x[1] // 2, 1 if target_x[0] > 0 else -1)
    guess_y = range(500)

    y_for_hits = [
        trace_probe((x, y), target_x, target_y) for x in guess_x for y in guess_y
    ]

    print(max(y_for_hits))


if __name__ == "__main__":
    main()
