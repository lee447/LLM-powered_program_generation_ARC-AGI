def solve(grid):
    H, W = len(grid), len(grid[0])
    center_r, center_c = (H - 1) / 2.0, (W - 1) / 2.0
    cands = []
    for r in range(1, H - 1):
        for c in range(1, W - 1):
            if grid[r][c] == 0 and grid[r-1][c] == 0 and grid[r+1][c] == 0 and grid[r][c-1] == 0 and grid[r][c+1] == 0:
                dist = abs(r - center_r) + abs(c - center_c)
                cands.append((dist, r, c))
    cands.sort(key=lambda x: (-x[0], x[1], x[2]))
    out = [row[:] for row in grid]
    for _, r, c in cands[:2]:
        for dr, dc in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
            out[r+dr][c+dc] = 3
    return out