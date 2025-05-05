from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                q=[(i,j)]
                vis[i][j]=True
                comp = {(i,j)}
                qi=0
                while qi<len(q):
                    r,c=q[qi]; qi+=1
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==1:
                            vis[nr][nc]=True
                            q.append((nr,nc))
                            comp.add((nr,nc))
                clusters.append(comp)
    clusters.sort(key=lambda c: len(c), reverse=True)
    out = [row[:] for row in grid]
    for idx, comp in enumerate(clusters):
        if idx==0:
            maxd=3
            color_map={1:6,2:8,3:2}
        else:
            maxd=1
            color_map={1:2}
        dil = [set(comp)]
        for d in range(1, maxd+1):
            prev = dil[d-1]
            nxt = set(prev)
            for (r,c) in prev:
                for dr in (-1,0,1):
                    for dc in (-1,0,1):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w:
                            nxt.add((nr,nc))
            dil.append(nxt)
        for d in range(1, maxd+1):
            ring = dil[d] - dil[d-1]
            col = color_map[d]
            for (r,c) in ring:
                if orig[r][c]!=1 and out[r][c]==orig[r][c]:
                    out[r][c]=col
    return out