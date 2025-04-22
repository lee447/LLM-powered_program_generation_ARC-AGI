def solve(grid):
    h = len(grid)
    w = len(grid[0])
    runs = []
    for r in range(h):
        for c in range(w-2):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r][c+2]==2:
                if (c==0 or grid[r][c-1]!=2) and (c+2==w-1 or grid[r][c+3]!=2):
                    runs.append((r,c))
    r0,c0 = runs[0]
    sr0 = h//2-1
    out = [row[:] for row in grid]
    for dr in range(3):
        for dc in range(3):
            out[sr0+dr][c0-2+dc] = 8
    return out
def solve(grid):
    h = len(grid)
    w = len(grid[0])
    runs = []
    for r in range(h):
        for c in range(w-2):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r][c+2]==2:
                if (c==0 or grid[r][c-1]!=2) and (c+2==w-1 or grid[r][c+3]!=2):
                    runs.append((r,c))
    r0,c0 = runs[0]
    sr0 = h//2-1
    out = [row[:] for row in grid]
    for dr in range(3):
        for dc in range(3):
            out[sr0+dr][c0-2+dc] = 8
    return out