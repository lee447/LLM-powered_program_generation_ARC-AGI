def solve(grid):
    N = len(grid[0])
    row0 = grid[0]
    c = row0.index(2)
    out = [[0]*N for _ in range(N)]
    red = []
    for i in range(N):
        if i <= c:
            j1, j2 = c - i, c + i
            out[i][j1] = 2
            out[i][j2] = 2
            red.append((i, j1))
            red.append((i, j2))
    blue = set()
    t = max(0, (c // 2))
    for i in range(N):
        if i < t: continue
        for j in range(N):
            if out[i][j] != 0: continue
            dr = min(abs(j - rj) for ri, rj in red if ri <= i)
            db = min(abs(j - bj) for bi, bj in blue) if blue else N
            if dr == 1 or db == 1:
                blue.add((i, j))
    for i, j in blue:
        out[i][j] = 1
    return out