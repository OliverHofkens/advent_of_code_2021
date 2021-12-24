#!/usr/bin/env python

import heapq
import sys
from functools import cache
from typing import Iterable, Iterator, List, Tuple

HallState = Tuple[str, ...]
RoomState = Tuple[str, str, str, str]
State = Tuple[HallState, RoomState]

ROOM_SIZE = 4


def parse_board_state(lines: List[str]) -> State:
    # The first and last lines are all wall:
    lines = lines[1:-1]
    hall = []
    rooms = []
    for idx, (hall_tile, occ_1, occ_2, occ_3, occ_4) in enumerate(zip(*lines)):
        if hall_tile == "#":
            continue
        if occ_1 == "#":
            # No room, so normal hallway tile:
            hall.append(hall_tile)
        else:
            # Room entrance, mark it:
            room_nr = len(rooms)
            hall.append(f"E{room_nr}")
            rooms.append(occ_4 + occ_3 + occ_2 + occ_1)

    return tuple(hall), tuple(rooms)


@cache
def reachable_hall_positions(hall: Tuple[str, ...], pos: int) -> Iterable[int]:
    reachable = []
    # Check forward:
    for i, pt in enumerate(hall[pos + 1 :], 1):
        if pt == "." or pt.startswith("E"):
            reachable.append(pos + i)
        else:
            break
    # Check backward:
    for i, pt in enumerate(hall[pos - 1 :: -1], 1):
        if pt == "." or pt.startswith("E"):
            reachable.append(pos - i)
        else:
            break
    return reachable


def move(
    state: State, src: Tuple[int, int], dest: Tuple[int, int]
) -> Tuple[int, State]:
    """
    Moves from src to dest in state.
    Returns:
        The cost and the new state
    """
    hall, rooms = state
    mut_hall = list(hall)
    mut_rooms = list(rooms)

    path_len = 0
    if src[0] == 0:
        piece = hall[src[1]]
        mut_hall[src[1]] = "."
        hall_start = src[1]
    else:
        piece = rooms[src[1]][-1]
        mut_rooms[src[1]] = rooms[src[1]][:-1]
        # The more occupants, the less we need to move to exit the room:
        path_len += (ROOM_SIZE + 1) - len(rooms[src[1]])
        hall_start = hall.index(f"E{src[1]}")

    if dest[0] == 0:
        mut_hall[dest[1]] = piece
        hall_end = dest[1]
    else:
        mut_rooms[dest[1]] += piece
        # The more occupants, the less we need to move to enter the room:
        path_len += ROOM_SIZE - len(rooms[dest[1]])
        hall_end = hall.index(f"E{dest[1]}")

    path_len += abs(hall_start - hall_end)
    # Shortcut! A = 0, D = 3, so the cost to move is 10^room_idx
    cost = path_len * 10 ** "ABCD".index(piece)
    return (cost, (tuple(mut_hall), tuple(mut_rooms)))


def find_possible_next_states(
    hall: Tuple[str, ...], rooms: Tuple[str, str, str, str]
) -> Iterator[Tuple[int, State]]:
    # Find any movable pieces in the hall:
    for i, piece in enumerate(hall):
        if piece in "ABCD":
            # A piece in the hall can only directly move to its preferred room:
            pref_room = "ABCD".index(piece)
            # If the room is occupied by someone else, can't move:
            if any(mem != piece for mem in rooms[pref_room]):
                continue
            # If the road to the room entrace is blocked, can't move:
            entrance = hall.index(f"E{pref_room}")
            start, end = (i + 1, entrance) if i < entrance else (entrance, i - 1)
            path = hall[start:end]
            if any(p in "ABCD" for p in path):
                continue

            # OK, we can move!
            yield move((hall, rooms), (0, i), (1, pref_room))

    # Find any movable pieces in the rooms:
    for room_idx, r in enumerate(rooms):
        if not r:
            # No one is here.
            continue
        piece = r[-1]
        pref_room = "ABCD".index(piece)
        if room_idx == pref_room and all(mem == piece for mem in r):
            # Already in preferred room and not in someone else's way
            continue

        # Find what we can reach:
        room_exit = hall.index(f"E{room_idx}")
        for hall_idx in reachable_hall_positions(hall, room_exit):
            hall_pos = hall[hall_idx]
            if hall_pos == ".":
                yield move((hall, rooms), (1, room_idx), (0, hall_idx))
            else:
                # If the reachable position is an entrance, we have to be able to
                # enter the room!
                room_ent = int(hall_pos[-1])
                if room_ent != pref_room:
                    continue
                if any(mem != piece for mem in rooms[room_ent]):
                    # Room is taken
                    continue

                yield move((hall, rooms), (1, room_idx), (1, pref_room))

                # After finding a room, there's no point in using other paths:
                break


def dijkstra_more_or_less(start_state: State) -> int:
    dists = {start_state: 0}
    states = [(0, *start_state)]
    heapq.heapify(states)

    while states:
        dist, hall, rooms = heapq.heappop(states)
        for move_cost, next_state in find_possible_next_states(hall, rooms):
            known_dist = dists.get(next_state, 1_000_000_000)
            alt = dist + move_cost
            if alt < known_dist:
                dists[next_state] = alt
                heapq.heappush(states, (alt, *next_state))

    # Return the best distance to the final state:
    empty_hall = tuple("." if pt in "ABCD" else pt for pt in hall)
    full_rooms = ("A" * ROOM_SIZE, "B" * ROOM_SIZE, "C" * ROOM_SIZE, "D" * ROOM_SIZE)
    return dists[(empty_hall, full_rooms)]


def main():
    initial_state = parse_board_state(sys.stdin.readlines())
    res = dijkstra_more_or_less(initial_state)
    print(res)


if __name__ == "__main__":
    main()
