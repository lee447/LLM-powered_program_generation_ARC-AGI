def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(H-1):
        for c in range(W-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                if c <= (W-1) - r:
                    out[r][c]=out[r][c+1]=out[r+1][c]=out[r+1][c+1]=8
    return out