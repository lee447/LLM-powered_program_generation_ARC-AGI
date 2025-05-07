from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 6 and not vis[i][j]:
                stk = [(i,j)]
                comp = []
                vis[i][j] = True
                while stk:
                    x,y = stk.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == 6:
                            vis[nx][ny] = True
                            stk.append((nx,ny))
                minc = min(y for x,y in comp)
                maxc = max(y for x,y in comp)
                for x,y in comp:
                    if y-minc <= maxc-y:
                        cc = y-1
                        while cc >= 0 and grid[x][cc] == 6:
                            cc -= 1
                        if cc >= 0:
                            res[x][y] = grid[x][cc]
                    else:
                        cc = y+1
                        while cc < w and grid[x][cc] == 6:
                            cc += 1
                        if cc < w:
                            res[x][y] = grid[x][cc]
    return res