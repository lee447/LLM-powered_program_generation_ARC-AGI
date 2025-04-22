from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    ones.sort()
    dr = ones[1][0] - ones[0][0]
    dc = ones[1][1] - ones[0][1]
    res = [row[:] for row in grid]
    last_r, last_c = ones[-1]
    while True:
        nr = last_r + dr
        nc = last_c + dc
        if 0 <= nr < h and 0 <= nc < w:
            res[nr][nc] = 2
            last_r, last_c = nr, nc
        else:
            break
    return res