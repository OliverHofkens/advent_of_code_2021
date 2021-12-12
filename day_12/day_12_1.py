#!/usr/bin/env python

import sys
from collections import defaultdict
from typing import Dict, List, Set

CaveMap = Dict[str, List[str]]
Route = List[str]


def optimize(graph: CaveMap):
    """
    Since we can only visit small caves once, we can remove
    any leaf nodes that are only connected by a small cave, as leaving that
    leaf node would make us pass through the small cave twice.
    """
    to_prune = []
    for start, dests in graph.items():
        # Leaf node and the only way is back through a small cave:
        if len(dests) == 1 and dests[0].islower() and start in graph[dests[0]]:
            to_prune.append((start, dests[0]))
    for prune in to_prune:
        del graph[prune[0]]
        graph[prune[1]].remove(prune[0])


def visit(system: CaveMap, cave: str, seen: Set[str], route: Route) -> List[Route]:
    route.append(cave)

    # If we made it to the end, hooray!
    if cave == "end":
        return [route]

    # Only visit small caves once:
    if cave.islower():
        seen.add(cave)

    destinations = [d for d in system[cave] if d not in seen]
    routes = []
    for d in destinations:
        routes.extend(visit(system, d, seen.copy(), route.copy()))
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

    optimize(graph)
    routes = visit(graph, "start", set(), [])
    print(len(routes))


if __name__ == "__main__":
    main()
