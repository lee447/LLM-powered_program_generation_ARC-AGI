def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    anchors = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==0 and grid[r][c+1]==0 and grid[r+1][c]==0 and grid[r+1][c+1]==0:
                anchors.append((r, c))
    out = [row[:] for row in grid]
    for r, c in anchors:
        end = r + 2
        if end > h: end = h
        for rr in range(end):
            out[rr][c] = 0
            out[rr][c+1] = 0
    return out