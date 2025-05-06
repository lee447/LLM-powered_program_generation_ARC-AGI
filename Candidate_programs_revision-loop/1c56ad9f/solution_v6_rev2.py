from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [[0]*W for _ in range(H)]
    # find the color
    color = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                color = grid[r][c]
                break
        if color:
            break
    # collect rows with any color
    rows = sorted({r for r in range(H) for c in range(W) if grid[r][c] == color})
    if not rows:
        return grid
    # find maximal contiguous run in each row
    max_run = 0
    runlen = {}
    for r in rows:
        cur = 0
        best = 0
        for c in range(W):
            if grid[r][c] == color:
                cur += 1
            else:
                best = max(best, cur)
                cur = 0
        best = max(best, cur)
        runlen[r] = best
        max_run = max(max_run, best)
    # mark full rows (the true horizontal lines)
    full = {r for r in rows if runlen[r] == max_run}
    # build the cycle of shifts
    cycle = [-1, 0, 1, 0]
    # assign shifts row by row
    idxs = {r:i for i,r in enumerate(rows)}
    for r in rows:
        idx = idxs[r]
        off = cycle[idx % 4]
        for c in range(W):
            if grid[r][c] == color:
                nc = c + off
                if 0 <= nc < W:
                    out[r][nc] = color
    return out