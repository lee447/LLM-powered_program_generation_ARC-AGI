def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c]==6 and not visited[r][c]:
                q = [(r,c)]
                visited[r][c]=True
                comp = []
                for x,y in q:
                    comp.append((x,y))
                    for dr,dc in dirs:
                        nr, nc = x+dr, y+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==6:
                            visited[nr][nc]=True
                            q.append((nr,nc))
                clusters.append(comp)
    res = [row[:] for row in grid]
    ref = [1,7,9]
    for comp in clusters:
        rows = sorted({r for r,c in comp})
        for r,c in comp:
            idx = rows.index(r)
            color = ref[idx] if idx<len(ref) else ref[-1]
            found=False
            for d in range(1,H+W):
                for dr in range(-d,d+1):
                    dc = d-abs(dr)
                    for sign in (-1,1) if dc else (1,):
                        rr,cc = r+dr, c+sign*dc
                        if 0<=rr<H and 0<=cc<W and grid[rr][cc]==color:
                            res[r][c]=color
                            found=True
                            break
                    if found: break
                if found: break
    return res