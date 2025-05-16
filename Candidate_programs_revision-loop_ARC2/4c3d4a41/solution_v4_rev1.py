from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not vis[i][j]:
                q=deque([(i,j)])
                vis[i][j]=True
                comp=[]
                while q:
                    r,c=q.popleft()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==5:
                            vis[nr][nc]=True
                            q.append((nr,nc))
                clusters.append(comp)
    if len(clusters)<2:
        return [row[:] for row in grid]
    big = max(clusters, key=len)
    small = min(clusters, key=len)
    out = [row[:] for row in grid]
    for r,c in small:
        out[r][c]=0
    big_cs = [c for _,c in big]
    small_cs = [c for _,c in small]
    big_cmin, big_cmax = min(big_cs), max(big_cs)
    small_cmin, small_cmax = min(small_cs), max(small_cs)
    interior_min = big_cmin+1
    interior_w = big_cmax - big_cmin - 1
    small_w = small_cmax - small_cmin + 1
    offset = interior_min + (interior_w - small_w)//2 - small_cmin
    for r,c in small:
        nc = c + offset
        out[r][nc] = 5
    return out