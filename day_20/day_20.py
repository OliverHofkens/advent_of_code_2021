#!/usr/bin/env python

import sys

from bitarray import bitarray
from bitarray.util import ba2int

ITERATIONS = 50


def _algo_idx(img, i, j, out_of_bounds: int = 0) -> int:
    idx_bits = bitarray()
    for row_idx in (i - 1, i, i + 1):
        try:
            row = img[row_idx]
        except IndexError:
            row = bitarray(3)
            row.setall(out_of_bounds)
            idx_bits.extend(row)
            continue

        if j == 0:
            cols = row[:2]
            cols.insert(0, out_of_bounds)
        elif j == len(row) - 1:
            cols = row[-2:]
            cols.append(out_of_bounds)
        else:
            cols = row[j - 1 : j + 2]
        idx_bits.extend(cols)
    return ba2int(idx_bits)


def enhance(img, algo, out_of_bounds: int = 0):
    # Only the first row/col out of bounds can change in an interesting way,
    # anything further than that is uniform. So expand our canvas by 1:
    fill_row = bitarray(len(img[0]) + 2)
    fill_row.setall(out_of_bounds)
    img = [fill_row] + img + [fill_row]
    # Pad left and right:
    for line in img[1:-1]:
        line.insert(0, out_of_bounds)
        line.append(out_of_bounds)

    # Don't want to modify the image while enhancing it.
    res = [line.copy() for line in img]
    for i in range(len(img)):
        for j in range(len(fill_row)):
            algo_idx = _algo_idx(img, i, j, out_of_bounds)
            res[i][j] = algo[algo_idx]

    return res


def main():
    lines = sys.stdin.readlines()
    algo = bitarray(lines[0].strip().replace("#", "1").replace(".", "0"))
    img = [
        bitarray(line.strip().replace("#", "1").replace(".", "0")) for line in lines[2:]
    ]

    # Enhance twice:
    out_of_bounds = 0
    for _ in range(ITERATIONS):
        img = enhance(img, algo, out_of_bounds)
        out_of_bounds = 0 if out_of_bounds else 1

    print(sum(line.count(1) for line in img))


if __name__ == "__main__":
    main()
