def solve(grid):
    n = len(grid)
    m = len(grid[0])
    grey = [(i,j) for i in range(n) for j in range(m) if grid[i][j]==5]
    rs = [i for i,j in grey]
    cs = [j for i,j in grey]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    key = None
    for i in range(r0, r1+1):
        for j in range(c0, c1+1):
            v = grid[i][j]
            if v!=5 and v!=0:
                key = v
                break
        if key is not None:
            break
    out = [row[:] for row in grid]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==key and not (r0<=i<=r1 and c0<=j<=c1):
                out[i][j] = 0
    return out