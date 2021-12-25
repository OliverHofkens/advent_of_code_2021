#!/usr/bin/env python

import operator
import sys
from typing import Callable, Sequence, Tuple, Union

KEEP = min
DIGITS = range(1, 10) if KEEP is max else range(9, 0, -1)

Var = Union[str, int]
Inp = str
Op = Tuple[Callable[[Var, Var], int], str, Var]
Instr = Union[Inp, Op]


def eql(a: int, b: int) -> int:
    return int(a == b)


OPS = {
    "add": operator.add,
    "div": operator.floordiv,
    "eql": eql,
    "mod": operator.mod,
    "mul": operator.mul,
}


def parse_instr(inp: str) -> Instr:
    parts = inp.split()
    if len(parts) == 2:
        return parts[1]
    op, a, b = parts
    try:
        b = int(b)
    except ValueError:
        pass
    return (OPS[op], a, b)


def MONAD(
    program: Sequence[Instr], state: Tuple[int, int, int, int], inp: int
) -> Tuple[int, int, int, int]:
    var = dict(zip("wxyz", state))
    for instr in program:
        if isinstance(instr, str):
            var[instr] = inp
        else:
            op, a, b = instr
            var[a] = op(var[a], b if isinstance(b, int) else var[b])

    return tuple(var.values())


def main():
    procedure = tuple(parse_instr(line) for line in sys.stdin.readlines())

    # From running a couple thousand numbers, it seems there are a ton of
    # duplicate states of the MONAD. So we cut down the search space by deduping
    # the states. So split up the procedure per input number first, so that we
    # can save unique states after each subprocedure.
    proc_parts = []
    last_pop = 0
    for i in range(len(procedure)):
        if isinstance(procedure[i], str) and i > 0:
            # This is an input, split the program here.
            proc_parts.append(procedure[last_pop:i])
            last_pop = i
    proc_parts.append(procedure[last_pop:])
    assert sum(len(p) for p in proc_parts) == len(procedure)

    # One model nr digit at a time, run the program until the next inp instruction
    # and keep the highest number that leads to that output state.
    # OPTIMIZATION: w is always the input, and x is always reset as first
    # instruction. So don't store them as unique states:
    states = {(0, 0): 0}
    for subproc in proc_parts:
        next_states = {}
        for s, current_best in states.items():
            for i in DIGITS:
                # 'append' the number to the right
                num = current_best * 10 + i
                out_state = MONAD(subproc, (0, 0, *s), i)
                next_states[out_state[2:]] = num
        states = next_states
        print(len(states), "unique states")

    keep = KEEP(model for state, model in states.items() if state[-1] == 0)
    print(keep)


if __name__ == "__main__":
    main()
