from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    greys = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 5]
    greys.sort()
    dr = greys[1][0] - greys[0][0]
    dc = greys[1][1] - greys[0][1]
    out = [row[:] for row in grid]
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            if v != 0 and v != 5:
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < R and 0 <= c2 < C and out[r2][c2] == 0:
                    out[r2][c2] = v
    return out