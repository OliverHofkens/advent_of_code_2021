#!/usr/bin/env python

import heapq
import sys
from typing import Iterator, List, Tuple

# A big int as placeholder for infinity
INT_INF = 1_000_000_000


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
    unseen = {(i, j) for i in range(height) for j in range(width)}
    dists = [[INT_INF] * width for _ in range(height)]

    source = (0, 0)
    dists[source[0]][source[1]] = 0

    verts = [(0, *source)]
    heapq.heapify(verts)

    while verts:
        dist, i, j = heapq.heappop(verts)

        for neighbor in _neighbors((i, j), width, height):
            if neighbor not in unseen:
                continue
            neighbor_dist = dists[neighbor[0]][neighbor[1]]
            alt = dist + map_[neighbor[0]][neighbor[1]]
            if alt < neighbor_dist:
                dists[neighbor[0]][neighbor[1]] = alt
                heapq.heappush(verts, (alt, *neighbor))

    return dists[-1][-1]


def inc_risk(tile: List[List[int]]) -> List[List[int]]:
    return [[x + 1 if x < 9 else 1 for x in row] for row in tile]


def main():
    risk_lvls = [[int(x) for x in row.strip()] for row in sys.stdin.readlines()]

    # The map grows 5x as large in both directions:
    tile = risk_lvls.copy()
    # Grow horizontally:
    for _ in range(4):
        tile = inc_risk(tile)
        for row, ext in zip(risk_lvls, tile):
            row.extend(ext)
    # Then grow vertically:
    tile = risk_lvls.copy()
    for _ in range(4):
        tile = inc_risk(tile)
        risk_lvls.extend(tile)

    lowest_cost = dijkstra(risk_lvls)
    print(lowest_cost)


if __name__ == "__main__":
    main()
