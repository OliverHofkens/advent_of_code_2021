#!/usr/bin/env python

import sys
from collections import Counter
from typing import Counter as TCounter
from typing import Dict


def polymerize_countwise(polymer: Counter, rules: Dict[str, str]) -> TCounter[str]:
    res: TCounter[str] = Counter()

    for template, count in polymer.items():
        # Each template AB turns into 2 new templates AC and CB:
        inject = rules[template]
        a = template[0] + inject
        b = inject + template[1]
        res[a] += count
        res[b] += count

    return res


def main():
    lines = sys.stdin.readlines()
    polymer_str = lines[0].strip()
    # Make a counter over the letter pairs:
    polymer_counter = Counter(a + b for a, b in zip(polymer_str, polymer_str[1:]))
    rules = dict(line.strip().split(" -> ") for line in lines[2:])

    for _ in range(40):
        polymer_counter = polymerize_countwise(polymer_counter, rules)

    # Turn the template counter into an element counter:
    elements = Counter()
    for (a, b), count in polymer_counter.items():
        elements[a] += count
    # The final letter appears ONCE more, as it always trails behind in the template pairs.
    elements[polymer_str[-1]] += 1
    counts = elements.most_common()
    print(counts[0][1] - counts[-1][1])


if __name__ == "__main__":
    main()
