#!/usr/bin/env python

import sys

ITERATIONS = 256


def main():
    counts = [0] * 9

    for age in sys.stdin.readline().split(","):
        counts[int(age)] += 1

    for i in range(ITERATIONS):
        # Decrease all counters by 1, but 0's become 6's:
        zeroes = counts.pop(0)
        counts[6] += zeroes
        # The amount of new ones is the same:
        counts.append(zeroes)

    print(sum(counts))


if __name__ == "__main__":
    main()
