#!/usr/bin/env python

import sys


def main():
    hits = [[0] * 1000 for _ in range(1000)]

    for line in sys.stdin.readlines():
        start, end = line.split("->")
        start_x, start_y = [int(n) for n in start.split(",")]
        end_x, end_y = [int(n) for n in end.split(",")]

        x_step = 1 if start_x <= end_x else -1
        y_step = 1 if start_y <= end_y else -1

        # Diagonal line
        if (start_x != end_x) and (start_y != end_y):
            # We're guaranteed diagonals of 45 degrees, so we know the ranges
            # are of equal length:
            for x, y in zip(
                range(start_x, end_x + x_step, x_step),
                range(start_y, end_y + y_step, y_step),
            ):
                hits[y][x] += 1

        # Orthogonal line
        else:
            for x in range(start_x, end_x + x_step, x_step):
                for y in range(start_y, end_y + y_step, y_step):
                    hits[y][x] += 1

    danger = 0
    for row in hits:
        for pt in row:
            if pt >= 2:
                danger += 1

    print(danger)


if __name__ == "__main__":
    main()
