from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    divider = next((j for j in range(w) if all(grid[i][j] == 5 for i in range(h))), None)
    if divider is None:
        return grid
    left_w = divider
    shift = divider + 1
    out = [row[:left_w] for row in grid]
    B0 = {(i, j) for i in range(h) for j in range(left_w) if out[i][j] == 0}
    colors = {grid[i][j] for i in range(h) for j in range(shift, w) if grid[i][j] not in (0, 5)}
    for c in colors:
        S = {(i, j - shift) for i in range(h) for j in range(shift, w) if grid[i][j] == c}
        if S == B0:
            for i, j in S:
                out[i][j] = c
            break
    return out