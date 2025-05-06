from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    res = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if not vis[y][x] and grid[y][x] in (1,8):
                stack = [(y,x)]
                comp = []
                c8 = 0
                vis[y][x] = True
                while stack:
                    cy, cx = stack.pop()
                    comp.append((cy,cx))
                    if grid[cy][cx] == 8:
                        c8 += 1
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx] in (1,8):
                            vis[ny][nx] = True
                            stack.append((ny,nx))
                if c8 <= 1:
                    for cy,cx in comp:
                        res[cy][cx] = grid[cy][cx]
    return res