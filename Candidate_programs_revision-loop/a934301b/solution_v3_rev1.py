from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    out = [[0]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != 0:
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                cnt8 = 0
                minx = maxx = i
                miny = maxy = j
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    if grid[x][y] == 8:
                        cnt8 += 1
                    minx = min(minx, x)
                    maxx = max(maxx, x)
                    miny = min(miny, y)
                    maxy = max(maxy, y)
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] != 0:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                height = maxx-minx+1
                width = maxy-miny+1
                if cnt8 <= 1 and height > 1 and width > 1 and len(comp) == height*width:
                    for x,y in comp:
                        out[x][y] = grid[x][y]
    return out