#!/usr/bin/env python

import sys


def main():
    hits = [[0] * 1000 for _ in range(1000)]

    for line in sys.stdin.readlines():
        start, end = line.split("->")
        start_x, start_y = [int(n) for n in start.split(",")]
        end_x, end_y = [int(n) for n in end.split(",")]

        # Only care for straight lines
        if (start_x != end_x) and (start_y != end_y):
            continue

        if start_x > end_x:
            start_x, end_x = end_x, start_x
        if start_y > end_y:
            start_y, end_y = end_y, start_y

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                hits[y][x] += 1

    danger = 0
    for row in hits:
        for pt in row:
            if pt >= 2:
                danger += 1

    print(danger)


if __name__ == "__main__":
    main()
