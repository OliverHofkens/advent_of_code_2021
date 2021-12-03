#!/usr/bin/env python

import sys
from typing import Iterable, Sequence, Tuple


def split_on_common_bit(
    inp: Iterable[str], bit_idx: int
) -> Tuple[Sequence[str], Sequence[str]]:
    """
    Splits `inp` in two lists, based on the most and least common bit at `bit_idx`.
    Returns:
        (most_common, least_common)
    """
    ones = []
    zeroes = []

    for bitline in inp:
        if bitline[bit_idx] == "0":
            zeroes.append(bitline)
        elif bitline[bit_idx] == "1":
            ones.append(bitline)

    if len(ones) > len(zeroes):
        return (ones, zeroes)
    elif len(zeroes) > len(ones):
        return (zeroes, ones)
    else:
        return (ones, zeroes)


def main():
    # Start off by splitting the input list in most_common and least_common:
    most_common, least_common = split_on_common_bit(sys.stdin.readlines(), 0)

    bit_idx = 1
    while len(most_common) > 1:
        most_common, _ = split_on_common_bit(most_common, bit_idx)
        bit_idx += 1

    bit_idx = 1
    while len(least_common) > 1:
        _, least_common = split_on_common_bit(least_common, bit_idx)
        bit_idx += 1

    oxygen_gen = int(most_common[0], 2)
    co2_scrubber = int(least_common[0], 2)
    print(oxygen_gen * co2_scrubber)


if __name__ == "__main__":
    main()
