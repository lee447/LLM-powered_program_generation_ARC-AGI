import sys
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    out = [[0]*cols for _ in range(rows)]
    j = 0
    while j < cols and grid[0][j] != 0:
        j += 1
    run = grid[0][:j]
    palette = []
    prev = None
    for v in run:
        if v != prev:
            palette.append(v)
            prev = v
    stray = None
    stray_col = None
    for k in range(j, cols):
        if grid[0][k] != 0:
            stray = grid[0][k]
            stray_col = k
            break
    if stray is not None:
        palette.append(stray)
    for k in range(j):
        out[0][k] = grid[0][k]
    if stray_col is not None:
        out[0][stray_col] = 5
    if rows > 1:
        out[1] = list(grid[1])
    cr = cc = None
    for i in range(2, rows):
        for k in range(cols):
            if grid[i][k] != 0:
                cr, cc = i, k
                break
        if cr is not None:
            break
    if cr is not None:
        for idx, color in enumerate(palette):
            r = idx
            if r == 0:
                out[cr][cc] = color
            else:
                top, bot = cr - r, cr + r
                left, right = cc - r, cc + r
                for x in range(left, right + 1):
                    if 0 <= top < rows and 0 <= x < cols:
                        out[top][x] = color
                    if 0 <= bot < rows and 0 <= x < cols:
                        out[bot][x] = color
                for y in range(top, bot + 1):
                    if 0 <= y < rows and 0 <= left < cols:
                        out[y][left] = color
                    if 0 <= y < rows and 0 <= right < cols:
                        out[y][right] = color
    return out