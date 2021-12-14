#!/usr/bin/env python

import sys
from collections import Counter
from typing import Dict


def polymerize(polymer: str, rules: Dict[str, str]) -> str:
    result = ""

    for a, b in zip(polymer, polymer[1:]):
        insert = rules[a + b]
        result += a + insert

    result += b
    return result


def main():
    lines = sys.stdin.readlines()
    polymer = lines[0].strip()
    rules = dict(line.strip().split(" -> ") for line in lines[2:])

    for _ in range(10):
        polymer = polymerize(polymer, rules)

    counts = Counter(polymer).most_common()
    print(counts[0][1] - counts[-1][1])


if __name__ == "__main__":
    main()
