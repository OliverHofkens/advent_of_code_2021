#!/usr/bin/env python

import sys
from collections import defaultdict
from typing import Dict, List, Optional, Set

CaveMap = Dict[str, List[str]]
Route = List[str]


def visit(
    system: CaveMap,
    cave: str,
    seen: Set[str],
    double_visit_choice: Optional[str],
    route: Route,
) -> List[Route]:
    # If we made it to the end, hooray!
    if cave == "end":
        route.append(cave)
        return [route]

    # Only visit small caves once:
    if cave.islower():
        # There is however, a single small cave we can visit twice:
        if cave != double_visit_choice or cave in route:
            seen.add(cave)

    route.append(cave)

    destinations = [d for d in system[cave] if d not in seen]
    routes = []
    for d in destinations:
        non_doubled = visit(system, d, seen.copy(), double_visit_choice, route.copy())
        # For a small cave, we can choose it as our "double visit" for this route
        # if we haven't chosen one already:
        if d.islower() and not double_visit_choice:
            doubled = visit(system, d, seen.copy(), d, route.copy())
            # There are cases where our choice doesn't matter, and just leads
            # to the same path as non_doubled. Check that here:
            doubled = [r for r in doubled if r not in non_doubled]
            routes.extend(doubled)

        routes.extend(non_doubled)
    return routes


def main():
    edges = [tuple(line.strip().split("-")) for line in sys.stdin.readlines()]

    graph = defaultdict(list)
    for a, b in edges:
        # We never want to move out of 'end' or into 'start'
        if a != "end" and b != "start":
            graph[a].append(b)
        if b != "end" and a != "start":
            graph[b].append(a)

    routes = visit(graph, "start", set(), None, [])
    print(len(routes))


if __name__ == "__main__":
    main()
