def solve(grid):
    h, w = len(grid), len(grid[0])
    ext = [[False]*w for _ in range(h)]
    q = []
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j] != 1 and not ext[i][j]:
                ext[i][j] = True
                q.append((i,j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j] != 1 and not ext[i][j]:
                ext[i][j] = True
                q.append((i,j))
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while q:
        r,c = q.pop()
        for dr,dc in dirs:
            rr,cc = r+dr, c+dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 1 and not ext[rr][cc]:
                ext[rr][cc] = True
                q.append((rr,cc))
    hole = [[grid[i][j] != 1 and not ext[i][j] for j in range(w)] for i in range(h)]
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if ext[i][j] and any(0 <= i+dr < h and 0 <= j+dc < w and grid[i+dr][j+dc] == 1 for dr,dc in dirs):
                out[i][j] = 2
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and any(0 <= i+dr < h and 0 <= j+dc < w and ext[i+dr][j+dc] for dr,dc in dirs):
                out[i][j] = 8
    for i in range(h):
        for j in range(w):
            if hole[i][j] and any(0 <= i+dr < h and 0 <= j+dc < w and grid[i+dr][j+dc] == 1 for dr,dc in dirs):
                out[i][j] = 6
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and any(0 <= i+dr < h and 0 <= j+dc < w and hole[i+dr][j+dc] for dr,dc in dirs):
                out[i][j] = 8
    return out