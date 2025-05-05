from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    div_col = grid[0].index(5)
    canvas = [row[:div_col] for row in grid]
    for r in range(h):
        for c in range(div_col+1, w):
            v = grid[r][c]
            if v != 0:
                new_c = c - div_col - 1
                if 0 <= new_c < div_col:
                    canvas[r][new_c] = v
    return canvas