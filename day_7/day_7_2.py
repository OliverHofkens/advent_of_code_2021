#!/usr/bin/env python

import sys


def fuel_consumption(distance: int) -> int:
    return distance * (distance + 1) // 2


def main():
    positions = [int(p) for p in sys.stdin.readline().split(",")]
    # Start off arbitrarily large:
    best_cost = 1_000_000_000_000

    for align in range(min(positions), max(positions)):
        fuel_cost = sum(fuel_consumption(abs(p - align)) for p in positions)
        if fuel_cost < best_cost:
            best_cost = fuel_cost

    print(best_cost)


if __name__ == "__main__":
    main()
