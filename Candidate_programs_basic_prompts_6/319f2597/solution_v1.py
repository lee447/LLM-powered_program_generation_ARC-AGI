def solve(grid):
    h = len(grid)
    w = len(grid[0])
    zeros = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==0]
    rows = sorted({r for r,_ in zeros})
    cols = sorted({c for _,c in zeros})
    out = [row[:] for row in grid]
    for r in rows:
        for c in range(w):
            if grid[r][c]!=2:
                out[r][c]=0
    for c in cols:
        for r in range(h):
            if grid[r][c]!=2:
                out[r][c]=0
    return out