def solve(grid):
    h=len(grid)
    w=len(grid[0])
    out=[row[:] for row in grid]
    bg=grid[0][0]
    marker=None
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=bg:
                marker=grid[r][c]
                break
        if marker is not None:
            break
    if marker is None:
        return out
    for r in range(h):
        cols=[c for c in range(w) if grid[r][c]==marker]
        cols.sort()
        for i in range(len(cols)-1):
            for c in range(cols[i]+1,cols[i+1]):
                out[r][c]=2
    return out