def solve(grid):
    n, m = len(grid), len(grid[0])
    # find block color
    from collections import Counter
    cnt = Counter(x for row in grid for x in row if x!=0)
    c = max(cnt, key=lambda v: cnt[v])
    # locate block bounds
    rows = [i for i in range(n) for j in range(m) if grid[i][j]==c]
    cols = [j for i in range(n) for j in range(m) if grid[i][j]==c]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    H, W = r1-r0+1, c1-c0+1
    out = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            # look left
            x, y = r0+i, c0+j-1
            if 0<=y and grid[x][y]!=c: out[i][j]=grid[x][y]; continue
            # look right
            x, y = r0+i, c1+j+1
            if y<m and grid[x][y]!=c: out[i][j]=grid[x][y]; continue
            # look up
            x, y = r0+i-1, c0+j
            if 0<=x and grid[x][y]!=c: out[i][j]=grid[x][y]; continue
            # look down
            x, y = r1+i+1, c0+j
            if x<n and grid[x][y]!=c: out[i][j]=grid[x][y]; continue
    return out