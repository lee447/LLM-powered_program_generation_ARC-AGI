def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(si,sj):
        q = [(si,sj)]
        comp = [(si,sj)]
        vis[si][sj] = True
        for i,j in q:
            for di,dj in dirs:
                ni, nj = i+di, j+dj
                if 0<=ni<h and 0<=nj<w and not vis[ni][nj] and grid[ni][nj]==5:
                    vis[ni][nj] = True
                    q.append((ni,nj))
                    comp.append((ni,nj))
        return comp
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not vis[i][j]:
                comp = bfs(i,j)
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                for r in range(r0, r1+1):
                    for c in range(c0, c1+1):
                        if out[r][c]==0:
                            out[r][c] = 2
    return out