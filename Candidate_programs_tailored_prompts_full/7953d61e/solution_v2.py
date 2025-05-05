from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    out = [[0] * (2*n) for _ in range(2*n)]
    rot_ccw = [[grid[c][n-1-r] for c in range(n)] for r in range(n)]
    rot_180 = [[grid[n-1-r][n-1-c] for c in range(n)] for r in range(n)]
    rot_cw = [[grid[n-1-c][r] for c in range(n)] for r in range(n)]
    for r in range(n):
        for c in range(n):
            out[r][c] = grid[r][c]
            out[r][c+n] = rot_ccw[r][c]
            out[r+n][c] = rot_180[r][c]
            out[r+n][c+n] = rot_cw[r][c]
    return out