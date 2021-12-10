#!/usr/bin/env python

import sys
from collections import deque
from statistics import median

CLOSERS = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORE_MAP = {"(": 1, "[": 2, "{": 3, "<": 4}


def main():
    all_scores = []
    stack = deque()

    for line in sys.stdin.readlines():
        line = line.rstrip()
        for char in line:
            try:
                closes = CLOSERS[char]
                if stack.pop() != closes:
                    # CORRUPT!
                    stack.clear()
                    break
            except KeyError:
                # Not a closer, so it's an opener:
                stack.append(char)

        if len(stack):
            score = 0
            # The line is incomplete, add the missing characters:
            for _ in range(len(stack)):
                to_close = stack.pop()
                score = score * 5 + SCORE_MAP[to_close]
            all_scores.append(score)

        stack.clear()

    print(median(all_scores))


if __name__ == "__main__":
    main()
