#!/usr/bin/env python

import sys


def main():
    depth = 0
    horizontal = 0

    for line in sys.stdin.readlines():
        action, amount = line.split()
        amount = int(amount)

        if action == "forward":
            horizontal += amount
        elif action == "down":
            depth += amount
        elif action == "up":
            depth -= amount
        else:
            raise NotImplementedError(action)

    print(depth * horizontal)


if __name__ == "__main__":
    main()
