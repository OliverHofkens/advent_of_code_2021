#!/usr/bin/env python

import sys


def main():
    total = 0

    depth_map = [[int(x) for x in row.strip()] for row in sys.stdin.readlines()]

    for i, row in enumerate(depth_map):
        for j, col in enumerate(row):
            north = 10 if i == 0 else depth_map[i - 1][j]
            south = 10 if i == len(depth_map) - 1 else depth_map[i + 1][j]
            east = 10 if j == len(row) - 1 else depth_map[i][j + 1]
            west = 10 if j == 0 else depth_map[i][j - 1]

            if col < north and col < south and col < east and col < west:
                total += 1 + col

    print(total)


if __name__ == "__main__":
    main()
