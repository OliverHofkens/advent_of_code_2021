#!/usr/bin/env python

import sys
from itertools import product


def main():
    energy = [[int(x) for x in row.strip()] for row in sys.stdin.readlines()]

    for step in range(1_000):
        flashes = []

        # First, all energies increase by 1:
        for i, row in enumerate(energy):
            for j, col in enumerate(row):
                if col == 9:
                    flashes.append((i, j))
                energy[i][j] += 1

        flash_idx = 0
        while flash_idx < len(flashes):
            # All octopi around the flash increase their energy by 1
            for i, j in flashes[flash_idx:]:
                for di, dj in product(range(i - 1, i + 2), range(j - 1, j + 2)):
                    # Bounds check:
                    if (
                        di < 0
                        or di > len(energy) - 1
                        or dj < 0
                        or dj > len(energy[0]) - 1
                    ):
                        continue

                    energy[di][dj] += 1
                    if energy[di][dj] > 9 and (di, dj) not in flashes:
                        flashes.append((di, dj))
                flash_idx += 1

        if len(flashes) == sum(len(row) for row in energy):
            print(step + 1)
            break

        # All energy levels that flashed become 0:
        for i, j in flashes:
            energy[i][j] = 0


if __name__ == "__main__":
    main()
