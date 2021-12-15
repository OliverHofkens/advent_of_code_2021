#!/usr/bin/env python

import sys
from typing import Iterator, List, Set, Tuple

# A big int as placeholder for infinity
INT_INF = 1_000_000_000


def _min_index_unseen(
    map_: List[List[int]], unseen: Set[Tuple[int, int]]
) -> Tuple[int, Tuple[int, int]]:
    current_min = INT_INF
    current_min_idx: Tuple[int, int]

    for i, j in unseen:
        risk = map_[i][j]
        if risk < current_min:
            current_min = risk
            current_min_idx = (i, j)

    return current_min, current_min_idx


def _neighbors(
    pt: Tuple[int, int], width: int, height: int
) -> Iterator[Tuple[int, int]]:
    i, j = pt
    if i > 0:
        yield (i - 1, j)
    if j < width - 1:
        yield (i, j + 1)
    if i < height - 1:
        yield (i + 1, j)
    if j > 0:
        yield (i, j - 1)


def dijkstra(map_: List[List[int]]) -> int:
    """
    Dijkstra's algorithm but the graph is a 2D array

    Returns:
        The cost of the lowest-cost path to the end.
    """
    width, height = len(map_[0]), len(map_)
    verts = {(i, j) for i in range(height) for j in range(width)}
    dists = [[INT_INF] * width for _ in range(height)]

    source = (0, 0)
    dists[source[0]][source[1]] = 0

    while verts:
        current_dist, current_pt = _min_index_unseen(dists, verts)
        verts.remove(current_pt)

        for neighbor in _neighbors(current_pt, width, height):
            if neighbor not in verts:
                continue
            neighbor_dist = dists[neighbor[0]][neighbor[1]]
            alt = current_dist + map_[neighbor[0]][neighbor[1]]
            if alt < neighbor_dist:
                dists[neighbor[0]][neighbor[1]] = alt

    return dists[-1][-1]


def main():
    risk_lvls = [[int(x) for x in row.strip()] for row in sys.stdin.readlines()]
    lowest_cost = dijkstra(risk_lvls)
    print(lowest_cost)


if __name__ == "__main__":
    main()
