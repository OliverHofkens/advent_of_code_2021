#!/usr/bin/env python

import sys
from itertools import count


def main():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]

    for step in count(1):
        # Check and move the EAST herd:
        moves_east = []
        for i, row in enumerate(grid):
            for j, spot in enumerate(row):
                if spot != ">":
                    continue
                dest = j + 1 if j < len(row) - 1 else 0
                if row[dest] != ".":
                    continue
                moves_east.append((i, j, dest))
        for i, j, dest in moves_east:
            grid[i][j] = "."
            grid[i][dest] = ">"

        # Check and move the SOUTH herd:
        moves_south = []
        for i, row in enumerate(grid):
            for j, spot in enumerate(row):
                if spot != "v":
                    continue
                dest = i + 1 if i < len(grid) - 1 else 0
                if grid[dest][j] != ".":
                    continue
                moves_south.append((i, j, dest))
        for i, j, dest in moves_south:
            grid[i][j] = "."
            grid[dest][j] = "v"

        if not moves_east and not moves_south:
            print(step)
            break


if __name__ == "__main__":
    main()
