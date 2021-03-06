# © 2020 지성. all rights reserved.
# <llllllllll@kakao.com>
# MIT License

import numpy as np

from dlgo import gotypes

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: ' . ',
    gotypes.Player.black: ' X ',
    gotypes.Player.white: ' O ',
}

# 다음 수 출력
def print_move(player, move):
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = f'{COLS[move.point.col - 1]}{move.point.row}'
    print(f'{str(player)} {move_str}')

# 현재 바둑판 현황 출력
def print_board(board):
    for row in range(board.num_rows, 0, -1):
        bump = ' ' if row <= 9 else ''
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print(f'{bump}{row} {"".join(line)}')
    print(f'{"    "}{"  ".join(COLS[:board.num_cols])}')

# 입력값을 좌표로 변환
def point_from_coords(coords):
    col = COLS.index(coords[0].upper()) + 1
    row = int(coords[1:])
    return gotypes.Point(row=row, col=col)

def coords_from_point(point):
    return f'{COLS[point.col -1]}{point.row}'

class MoveAge():
    def __init__(self, board):
        self.move_ages = - np.ones((board.num_rows, board.num_cols))

    def get(self, row, col):
        return self.move_ages[row, col]

    def reset_age(self, point):
        self.move_ages[point.row - 1, point.col - 1] = -1

    def add(self, point):
        self.move_ages[point.row - 1, point.col - 1] = 0

    def increment_all(self):
        self.move_ages[self.move_ages > -1] += 1