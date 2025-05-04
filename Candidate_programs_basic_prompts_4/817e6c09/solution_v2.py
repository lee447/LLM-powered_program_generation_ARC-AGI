def solve(grid):
    h = len(grid)
    w = len(grid[0])
    tl = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                tl.append((r,c))
    pts = sorted(tl, key=lambda x:(-x[0], x[1]))
    n = len(pts)
    dp = [1]*n
    par = [-1]*n
    best = 0
    bi = 0
    for i in range(n):
        for j in range(i):
            if pts[j][1] <= pts[i][1] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                par[i] = j
        if dp[i] > best:
            best = dp[i]
            bi = i
    sel = set()
    cur = bi
    while cur != -1:
        sel.add(pts[cur])
        cur = par[cur]
    res = [row[:] for row in grid]
    for r,c in tl:
        if (r,c) in sel:
            for dr in (0,1):
                for dc in (0,1):
                    res[r+dr][c+dc] = 8
    return res