from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    divider = next((j for j in range(w) if all(grid[i][j] == 5 for i in range(h))), None)
    if divider is None:
        return []
    left_w = divider
    canvas = [row[:left_w][:] for row in grid]
    shift = divider + 1
    for i in range(h):
        for j in range(shift, w):
            v = grid[i][j]
            if v != 0 and v != 5:
                nj = j - shift
                if 0 <= nj < left_w:
                    canvas[i][nj] = v
    return canvas