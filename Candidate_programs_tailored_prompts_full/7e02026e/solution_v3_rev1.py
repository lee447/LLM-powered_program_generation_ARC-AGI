from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                comp = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==0:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                if len(comp)==9:
                    rs = [p[0] for p in comp]
                    cs = [p[1] for p in comp]
                    if max(rs)-min(rs)==2 and max(cs)-min(cs)==2:
                        minr, minc = min(rs), min(cs)
                        mr, mc = minr+1, minc+1
                        for dr,dc in ((0,0),(-1,0),(1,0),(0,-1),(0,1)):
                            res[mr+dr][mc+dc] = 3
    return res