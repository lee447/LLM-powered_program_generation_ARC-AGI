def solve(grid):
    h = len(grid)
    w = len(grid[0])
    r0 = c0 = None
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] == 2 and grid[r-1][c] == 2 and grid[r+1][c] == 2 and grid[r][c-1] == 2 and grid[r][c+1] == 2:
                r0, c0 = r, c
                break
        if r0 is not None:
            break
    out = [[0] * w for _ in range(h)]
    for dr, dc in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]:
        out[r0+dr][c0+dc] = 2
    m = min(r0, c0, h-1-r0, w-1-c0)
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        for k in range(1, m):
            out[r0+dr*k][c0+dc*k] = 8
        out[r0+dr*m][c0+dc*m] = 4
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        k = 1
        while 0 <= r0+dr*k < h and 0 <= c0+dc*k < w:
            if out[r0+dr*k][c0+dc*k] == 0:
                out[r0+dr*k][c0+dc*k] = 1
            k += 1
    return out