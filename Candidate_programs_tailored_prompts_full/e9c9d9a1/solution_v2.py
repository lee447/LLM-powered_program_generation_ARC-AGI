def solve(grid):
    R=len(grid); C=len(grid[0])
    res=[row[:] for row in grid]
    hlines=[r for r in range(R) if all(grid[r][c]==3 for c in range(C))]
    vlines=[c for c in range(C) if all(grid[r][c]==3 for r in range(R))]
    first_h, last_h = hlines[0], hlines[-1]
    first_v, last_v = vlines[0], vlines[-1]
    for r in range(0, first_h):
        for c in range(0, first_v):
            if res[r][c]==0: res[r][c]=2
        for c in range(last_v+1, C):
            if res[r][c]==0: res[r][c]=4
    for r in range(first_h+1, last_h):
        for c in range(first_v+1, last_v):
            if res[r][c]==0: res[r][c]=7
    for r in range(last_h+1, R):
        for c in range(0, first_v):
            if res[r][c]==0: res[r][c]=1
        for c in range(last_v+1, C):
            if res[r][c]==0: res[r][c]=8
    return res