def solve(grid):
    h=len(grid)
    w=len(grid[0]) if h else 0
    res=[row[:] for row in grid]
    last=h-1
    stripe_cols=[c for c in range(w) if grid[last][c]!=0]
    for c in stripe_cols:
        for r in range(h):
            for i in range(r,h):
                if grid[i][c]!=0:
                    res[r][c]=grid[i][c]
                    break
    return res