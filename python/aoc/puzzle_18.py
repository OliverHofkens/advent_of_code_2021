#!/usr/bin/env python

import sys
from typing import List, Tuple


def find_basin_size(depth_map: List[List[int]], low_i: int, low_j: int) -> int:
    basin_points: List[Tuple[int, int]] = [(low_i, low_j)]
    progress_idx: int = 0

    while progress_idx < len(basin_points):
        for i, j in basin_points[progress_idx:]:
            if i > 0 and depth_map[i - 1][j] < 9:
                north_coord = (i - 1, j)
                if north_coord not in basin_points:
                    basin_points.append(north_coord)

            if i < len(depth_map) - 1 and depth_map[i + 1][j] < 9:
                south_coord = (i + 1, j)
                if south_coord not in basin_points:
                    basin_points.append(south_coord)

            if j < len(depth_map[0]) - 1 and depth_map[i][j + 1] < 9:
                east_coord = (i, j + 1)
                if east_coord not in basin_points:
                    basin_points.append(east_coord)

            if j > 0 and depth_map[i][j - 1] < 9:
                west_coord = (i, j - 1)
                if west_coord not in basin_points:
                    basin_points.append(west_coord)

            progress_idx += 1

    print(f"Basin finished! Size {len(basin_points)}")
    return len(basin_points)


def main():
    depth_map = [[int(x) for x in row.strip()] for row in sys.stdin.readlines()]

    basin_sizes = []

    for i, row in enumerate(depth_map):
        for j, col in enumerate(row):
            north = 9 if i == 0 else depth_map[i - 1][j]
            south = 9 if i == len(depth_map) - 1 else depth_map[i + 1][j]
            east = 9 if j == len(row) - 1 else depth_map[i][j + 1]
            west = 9 if j == 0 else depth_map[i][j - 1]

            if col < north and col < south and col < east and col < west:
                # Low point! Find the size of the basin:
                basin_sizes.append(find_basin_size(depth_map, i, j))

    basins = sorted(basin_sizes, reverse=True)
    print(basins[0] * basins[1] * basins[2])


if __name__ == "__main__":
    main()
