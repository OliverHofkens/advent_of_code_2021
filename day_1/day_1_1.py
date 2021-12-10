#!/usr/bin/env python

import sys


def main():
    # Start off arbitrarily large, so the first measurement is not counted as an
    # increase.
    last_measurement: int = 1_000_000_000
    num_increases: int = 0

    for line in sys.stdin.readlines():
        measurement = int(line)
        if measurement > last_measurement:
            num_increases += 1
        last_measurement = measurement

    print(num_increases)


if __name__ == "__main__":
    main()
