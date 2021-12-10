#!/usr/bin/env python

import sys


def main():
    aim = 0
    depth = 0
    horizontal = 0

    for line in sys.stdin.readlines():
        action, amount = line.split()
        amount = int(amount)

        match action:
            case "forward":
                horizontal += amount
                depth += aim * amount
            case "down":
                aim += amount
            case "up":
                aim -= amount
            case _:
                raise NotImplementedError(action)

    print(depth * horizontal)


if __name__ == "__main__":
    main()
