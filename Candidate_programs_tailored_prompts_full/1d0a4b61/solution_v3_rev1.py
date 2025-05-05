import typing
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    bc = grid[0][0]
    for height in range(1, h):
        if all(cell == bc for cell in grid[height]):
            hp = height
            break
    for width in range(1, w):
        if all(grid[r][width] == bc for r in range(h)):
            wp = width
            break
    pattern = [[None] * wp for _ in range(hp)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                pr = r % hp
                pc = c % wp
                if pattern[pr][pc] is None:
                    pattern[pr][pc] = v
    for pr in range(hp):
        for pc in range(wp):
            if pattern[pr][pc] is None:
                for r in range(pr, h, hp):
                    for c in range(pc, w, wp):
                        v = grid[r][c]
                        if v != 0:
                            pattern[pr][pc] = v
                            break
                    if pattern[pr][pc] is not None:
                        break
    res = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            res[r][c] = v if v != 0 else pattern[r % hp][c % wp]
    return res