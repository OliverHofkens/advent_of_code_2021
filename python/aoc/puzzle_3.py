#!/usr/bin/env python

import sys


def main():
    depth = 0
    horizontal = 0

    for line in sys.stdin.readlines():
        action, amount = line.split()
        amount = int(amount)

        match action:
            case "forward":
                horizontal += amount
            case "down":
                depth += amount
            case "up":
                depth -= amount
            case _:
                raise NotImplementedError(action)

    print(depth * horizontal)


if __name__ == "__main__":
    main()
