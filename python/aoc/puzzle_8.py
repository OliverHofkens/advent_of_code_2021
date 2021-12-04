#!/usr/bin/env python

import sys
from typing import List


class BingoBoard:
    def __init__(self, boards_numbers: List[List[int]]):
        self.numbers = boards_numbers
        self.hits = [[False for _ in range(len(row))] for row in boards_numbers]

    def mark(self, number: int):
        for i, row in enumerate(self.numbers):
            for j, board_num in enumerate(row):
                if board_num == number:
                    self.hits[i][j] = True

    def won(self) -> bool:
        # Check if any row is complete:
        if any(all(r) for r in self.hits):
            return True

        # Check if any column is complete:
        for col in range(len(self.hits[0])):
            if all(r[col] for r in self.hits):
                return True

        return False

    def score(self) -> int:
        score = 0
        for i, row in enumerate(self.hits):
            for j, hit in enumerate(row):
                if not hit:
                    score += self.numbers[i][j]

        return score


def main():
    lines = sys.stdin.readlines()
    draw_sequence = iter(int(n) for n in lines[0].split(","))

    boards = []
    board_buf = []
    for line in lines[2:]:
        if line == "\n":
            boards.append(BingoBoard(board_buf))
            board_buf = []
            continue

        board_buf.append([int(num) for num in line.split()])

    # If any leftovers in board_buf, finish that board:
    if board_buf:
        boards.append(BingoBoard(board_buf))

    # Start the bingo:
    for draw in draw_sequence:
        elim = []

        for board in boards:
            board.mark(draw)
            if board.won():
                if len(boards) > 1:
                    elim.append(board)
                else:
                    print(board.score() * draw)
                    return

        for b in elim:
            boards.remove(b)


if __name__ == "__main__":
    main()
