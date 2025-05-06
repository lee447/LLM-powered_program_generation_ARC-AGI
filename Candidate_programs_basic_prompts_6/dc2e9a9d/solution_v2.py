def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 3 and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                cells = []
                rmin=rmax=i; cmin=cmax=j
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    rmin = min(rmin, r); rmax = max(rmax, r)
                    cmin = min(cmin, c); cmax = max(cmax, c)
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<H and 0<=cc<W and not seen[rr][cc] and grid[rr][cc]==3:
                            seen[rr][cc] = True
                            q.append((rr,cc))
                shape = set((r-rmin, c-cmin) for r,c in cells)
                clusters.append((rmin,cmin,rmax,cmax,shape))
    clusters.sort(key=lambda x: x[0])
    out = [row[:] for row in grid]
    if len(clusters) >= 1:
        r0,c0,r1,c1,sh = clusters[0]
        h = r1-r0+1; w = c1-c0+1
        nc = c1+2
        if nc+w-1 < W:
            for dr,dc in sh:
                out[r0+dr][nc+dc] = 1
    if len(clusters) >= 2:
        r0,c0,r1,c1,sh = clusters[1]
        h = r1-r0+1; w = c1-c0+1
        up = r0 - h - 1
        if up >= 0:
            rr = up
        else:
            rr = r1 + 2
        if 0 <= rr and rr+h-1 < H:
            for dr,dc in sh:
                out[rr+dr][c0+dc] = 8
    return out