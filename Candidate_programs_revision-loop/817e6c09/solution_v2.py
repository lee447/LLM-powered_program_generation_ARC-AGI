def solve(grid):
    import math
    H, W = len(grid), len(grid[0])
    tls = []
    for r in range(H-1):
        for c in range(W-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                tls.append((r,c))
    n = len(tls)
    if n==0:
        return grid
    centers = []
    cy = H/2
    cx = W/2
    for (r,c) in tls:
        y = r+0.5 - cy
        x = c+0.5 - cx
        centers.append(math.atan2(y, x))
    paired = list(zip(centers, tls))
    paired.sort()
    angs = [a for a,_ in paired]
    pos = [p for _,p in paired]
    K = (n+1)//2
    ext = angs + [a+2*math.pi for a in angs]
    best_i = 0
    if K*2 <= n:
        best_span = float('inf')
        for i in range(n):
            span = ext[i+K-1] - ext[i]
            if span < best_span:
                best_span = span
                best_i = i
    else:
        best_span = -1.0
        for i in range(n):
            span = ext[i+K-1] - ext[i]
            if span > best_span:
                best_span = span
                best_i = i
    sel = set()
    for j in range(best_i, best_i+K):
        sel.add(pos[j % n])
    out = [row[:] for row in grid]
    for (r,c) in sel:
        out[r][c] = 8
        out[r][c+1] = 8
        out[r+1][c] = 8
        out[r+1][c+1] = 8
    return out