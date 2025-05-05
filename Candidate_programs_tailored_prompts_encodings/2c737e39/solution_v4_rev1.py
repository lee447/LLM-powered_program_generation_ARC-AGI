from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    if len(greys) != 2:
        return [row[:] for row in grid]
    (r1, c1), (r2, c2) = greys
    dr, dc = r2 - r1, c2 - c1
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != 5:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == 0:
                    out[nr][nc] = v
    out[r2][c2] = 0
    return out