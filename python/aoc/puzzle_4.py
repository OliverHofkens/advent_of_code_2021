#!/usr/bin/env python

import sys


def main():
    aim = 0
    depth = 0
    horizontal = 0

    for line in sys.stdin.readlines():
        action, amount = line.split()
        amount = int(amount)

        if action == "forward":
            horizontal += amount
            depth += aim * amount
        elif action == "down":
            aim += amount
        elif action == "up":
            aim -= amount
        else:
            raise NotImplementedError(action)

    print(depth * horizontal)


if __name__ == "__main__":
    main()
