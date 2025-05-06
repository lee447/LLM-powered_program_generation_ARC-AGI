from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zeros = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 0]
    rs = [r for r, c in zeros]
    cs = [c for r, c in zeros]
    r_min, r_max = min(rs), max(rs)
    c_min, c_max = min(cs), max(cs)
    dist_up = r_min
    dist_down = H - 1 - r_max
    dist_left = c_min
    dist_right = W - 1 - c_max
    vert = 'up' if dist_up < dist_down else 'down'
    horiz = 'left' if dist_left < dist_right else 'right'
    res = [row[:] for row in grid]
    if vert == 'up':
        for r in range(0, r_min):
            for c in range(c_min, c_max + 1):
                res[r][c] = 0
    else:
        for r in range(r_max + 1, H):
            for c in range(c_min, c_max + 1):
                res[r][c] = 0
    if horiz == 'left':
        for r in range(r_min, r_max + 1):
            for c in range(0, c_min):
                res[r][c] = 0
    else:
        for r in range(r_min, r_max + 1):
            for c in range(c_max + 1, W):
                res[r][c] = 0
    return res