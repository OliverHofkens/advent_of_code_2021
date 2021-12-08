#!/usr/bin/env python

import sys


def main():
    counts = [0] * 10

    for line in sys.stdin.readlines():
        uniq, to_guess = line.split("|")
        guess_digits = to_guess.split()

        # For this part we only need `to_guess` as we only look for the digits with
        # unique signatures.
        for dig in guess_digits:
            if len(dig) == 2:
                counts[1] += 1
            elif len(dig) == 4:
                counts[4] += 1
            elif len(dig) == 3:
                counts[7] += 1
            elif len(dig) == 7:
                counts[8] += 1

    print(counts[1] + counts[4] + counts[7] + counts[8])


if __name__ == "__main__":
    main()
