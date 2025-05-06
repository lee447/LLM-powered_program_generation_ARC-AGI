from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for i in range(h):
        for j in range(w):
            cnt[grid[i][j]] = cnt.get(grid[i][j], 0) + 1
    bg = max(cnt, key=lambda x: cnt[x])
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != bg:
                c = grid[i][j]
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == c:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                shapes.append(comp)
    shapes.sort(key=lambda comp: min(x for x,_ in comp))
    out = [[bg]*w for _ in range(h)]
    for idx, comp in enumerate(shapes):
        d = -1 if idx % 2 == 0 else 1
        color = grid[comp[0][0]][comp[0][1]]
        for x,y in comp:
            out[x][y+d] = color
    return out