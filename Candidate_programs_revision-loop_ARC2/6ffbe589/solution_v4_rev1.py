from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                comps.append(comp)
    if not comps:
        return []
    comp = max(comps, key=len)
    rs = [r for r,c in comp]
    cs = [c for r,c in comp]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
    H, W = len(sub), len(sub[0])
    S = max(H, W)
    dh = S - H
    dw = S - W
    top = dh // 2
    bottom = dh - top
    left = dw // 2
    right = dw - left
    new = [[0]*S for _ in range(top)]
    for row in sub:
        new.append([0]*left + row + [0]*right)
    new += [[0]*S for _ in range(bottom)]
    return new