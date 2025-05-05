from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    greys = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 5]
    greys.sort()
    sr, sc = greys[0]
    tr, tc = greys[1]
    dr, dc = tr - sr, tc - sc
    out = [row[:] for row in grid]
    out[tr][tc] = 0
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            if v != 0 and v != 5:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and out[nr][nc] == 0:
                    out[nr][nc] = v
    return out