#!/usr/bin/env python

import sys
from collections import deque

CLOSERS = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORE_MAP = {")": 3, "]": 57, "}": 1197, ">": 25137}


def main():
    score = 0
    stack = deque()

    for line in sys.stdin.readlines():
        for char in line:
            try:
                closes = CLOSERS[char]
                if stack.pop() != closes:
                    # CORRUPT!
                    score += SCORE_MAP[char]
                    break
            except KeyError:
                # Not a closer, so it's an opener:
                stack.append(char)

        stack.clear()

    print(score)


if __name__ == "__main__":
    main()
