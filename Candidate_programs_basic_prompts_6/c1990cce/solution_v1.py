def solve(grid):
    n = len(grid[0])
    r0 = 0
    c0 = grid[0].index(2)
    out = [[0]*n for _ in range(n)]
    for i in range(n):
        d = abs(i - r0)
        if d <= c0: out[i][c0-d] = 2
        if c0+d < n: out[i][c0+d] = 2
    k = n//2
    for i in range(n):
        for j in range(n):
            if out[i][j]==0 and out[k][j]==0 and abs(i-k)+abs(j-k)>=k%2 and abs(i-k)+abs(j-k)<=k:
                out[i][j] = 1
    return out