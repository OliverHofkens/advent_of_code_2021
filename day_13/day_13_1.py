#!/usr/bin/env python

import sys
from typing import List, Tuple


def _parse_fold(fold_desc: str) -> Tuple[str, int]:
    axis, at = fold_desc.split("=")
    return (axis[-1], int(at))


def fold(fold: Tuple[str, int], points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    axis, fold_at = fold
    fold_idx = 0 if axis == "x" else 1
    # We're only moving points below or to the right of the fold:
    moving = [p for p in points if p[fold_idx] > fold_at]
    result = [p for p in points if p[fold_idx] < fold_at]

    for pt in moving:
        diff = pt[fold_idx] - 2 * (pt[fold_idx] - fold_at)
        result.append((pt[0] if axis == "y" else diff, pt[1] if axis == "x" else diff))

    return result


def main():
    lines = sys.stdin.readlines()
    split_idx = lines.index("\n")
    points = [tuple(int(x) for x in line.split(",")) for line in lines[:split_idx]]
    folds = [_parse_fold(line) for line in lines[split_idx + 1 :]]

    # For part 1, only consider the first fold:
    points = fold(folds[0], points)
    print(len(set(points)))


if __name__ == "__main__":
    main()
