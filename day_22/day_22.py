#!/usr/bin/env python

import sys
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

Range = Tuple[int, int]


@dataclass
class Cuboid:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    subtracted: List["Cuboid"] = field(default_factory=list)

    def volume(self) -> int:
        total_vol = (
            (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)
        )
        subtracted_vol = sum(sub.volume() for sub in self.subtracted)
        res = total_vol - subtracted_vol
        return res

    def subtract(self, other: "Cuboid") -> Optional["Cuboid"]:
        overlap_x = (max(self.x1, other.x1), min(self.x2, other.x2))
        overlap_y = (max(self.y1, other.y1), min(self.y2, other.y2))
        overlap_z = (max(self.z1, other.z1), min(self.z2, other.z2))

        if any(o[0] > o[1] for o in (overlap_x, overlap_y, overlap_z)):
            # No overlap, self remains whole:
            return self
        elif (
            overlap_x == (self.x1, self.x2)
            and overlap_y == (self.y1, self.y2)
            and overlap_z == (self.z1, self.z2)
        ):
            # Complete overlap, nothing remains:
            return None
        else:
            # Partial overlap, sub the intersection from self and all previously
            # subtracted cuboids:
            intersection = Cuboid(*overlap_x, *overlap_y, *overlap_z)
            self.subtracted = list(
                filter(None, (c.subtract(intersection) for c in self.subtracted))
            )
            self.subtracted.append(intersection)
            if self.volume() <= 0:
                return None
            return self


def parse_range(inp: str) -> Range:
    axis, limits = inp.split("=")
    return tuple(int(lim) for lim in limits.split(".."))


def parse_step(inp: str) -> Tuple[bool, Range, Range, Range]:
    action, ranges_str = inp.split()
    ranges = [parse_range(r) for r in ranges_str.split(",")]
    return (action == "on", *ranges)


def main():
    steps = [parse_step(line) for line in sys.stdin.readlines()]
    cuboids = []
    for add, x_range, y_range, z_range in steps:
        # Part 1:
        # if any(r[0] < -50 or r[1] > 50 for r in (x_range, y_range, z_range)):
        #     continue

        cube = Cuboid(*x_range, *y_range, *z_range)
        # Intersect this cube with all others:
        cuboids = list(filter(None, (c.subtract(cube) for c in cuboids)))
        if add:
            cuboids.append(cube)

    print(sum(c.volume() for c in cuboids))


if __name__ == "__main__":
    main()
