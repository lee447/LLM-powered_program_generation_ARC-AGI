def solve(grid):
    h,len0 = len(grid), len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(len0):
            v = grid[i][j]
            if v:
                counts[v] = counts.get(v, 0) + 1
    C = max(counts, key=lambda k: counts[k])
    minr, maxr, minc, maxc = h, -1, len0, -1
    for i in range(h):
        for j in range(len0):
            if grid[i][j] == C:
                minr = min(minr, i); maxr = max(maxr, i)
                minc = min(minc, j); maxc = max(maxc, j)
    H = maxr - minr + 1; W = maxc - minc + 1
    res = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i==0 or i==H-1 or j==0 or j==W-1:
                res[i][j] = C
    keep = [any(res[i][j]!=0 for i in range(H)) for j in range(W)]
    out = [[res[i][j] for j in range(W) if keep[j]] for i in range(H)]
    return out