def solve(grid):
    from collections import Counter
    border = grid[0][0]
    rows = [r[:] for r in grid if border not in r]
    cnt = Counter(c for r in rows for c in r if c!=border)
    motif_color = min((c for c,n in cnt.items() if n>1), key=lambda c: cnt[c])
    R, C = len(rows), len(rows[0])
    minr = minc = 10**9
    maxr = maxc = -1
    for i in range(R):
        for j in range(C):
            if rows[i][j]==motif_color:
                minr = min(minr,i); maxr = max(maxr,i)
                minc = min(minc,j); maxc = max(maxc,j)
    h = maxr-minr+1; w = maxc-minc+1
    left = minc
    right = minc+maxc-1
    for i0 in range(0,minr+1,h):
        for di in range(h):
            for dj in range(w):
                rows[i0+di][left+dj] = motif_color
                rows[i0+di][right+dj] = motif_color
    for j0 in range(left,right+1,w):
        for di in range(h):
            for dj in range(w):
                rows[minr+di][j0+dj] = motif_color
    return rows