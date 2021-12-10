#!/usr/bin/env python

import sys
from typing import List


class RingBuf:
    """Simple implementation of a ring buffer"""

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.vals: List[int] = []
        self.head: int = 0

    def append(self, item: int):
        if len(self.vals) < self.capacity:
            self.vals.append(item)
        else:
            self.vals[self.head] = item
            self.head += 1
            if self.head > self.capacity - 1:
                self.head = 0


def main():
    CAPACITY = 3

    # Start off arbitrarily large, so the first measurement is not counted as an
    # increase.
    last_measurement: int = 1_000_000_000
    num_increases: int = 0
    ring_buf = RingBuf(CAPACITY)

    lines = sys.stdin.readlines()

    # Initialize the ring buffer:
    ring_buf.vals = [int(l) for l in lines[:3]]

    for line in lines[3:]:
        ring_buf.append(int(line))
        moving_sum = sum(ring_buf.vals)

        if moving_sum > last_measurement:
            num_increases += 1
        last_measurement = moving_sum

    print(num_increases)


if __name__ == "__main__":
    main()
