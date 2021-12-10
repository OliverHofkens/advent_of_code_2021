#!/usr/bin/env python

import sys

INPUT_LENGTH = 12


def main():
    count_zero = [0] * INPUT_LENGTH
    count_one = [0] * INPUT_LENGTH

    for line in sys.stdin.readlines():
        for idx, bit in enumerate(line):
            if bit == "0":
                count_zero[idx] += 1
            elif bit == "1":
                count_one[idx] += 1

    gamma_rate = 0
    epsilon_rate = 0
    for i in range(len(count_zero)):
        if count_one[i] > count_zero[i]:
            gamma_rate = (gamma_rate << 1) | 1
            epsilon_rate = epsilon_rate << 1
        else:
            gamma_rate = gamma_rate << 1
            epsilon_rate = (epsilon_rate << 1) | 1

    print(gamma_rate * epsilon_rate)


if __name__ == "__main__":
    main()
