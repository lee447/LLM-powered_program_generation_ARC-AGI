from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c == 0 or vis[i][j]:
                continue
            stack = [(i, j)]
            comp = []
            vis[i][j] = True
            while stack:
                x, y = stack.pop()
                comp.append((x, y))
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == c:
                        vis[nx][ny] = True
                        stack.append((nx, ny))
            minr = min(x for x, _ in comp)
            maxr = max(x for x, _ in comp)
            minc = min(y for _, y in comp)
            maxc = max(y for _, y in comp)
            H, W = maxr - minr + 1, maxc - minc + 1
            ok = True
            for x, y in comp:
                if not (x == minr or x == maxr or y == minc or y == maxc):
                    ok = False
                    break
            if not ok:
                continue
            for ii in range(minr+1, maxr):
                for jj in range(minc+1, maxc):
                    if grid[ii][jj] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                shapes.append((minr, minc, H, W))
    if not shapes:
        return [[]]
    shapes.sort(key=lambda x: (-x[2]*x[3], x[0], x[1]))
    minr, minc, H, W = shapes[0]
    res = [[grid[minr+i][minc+j] if (i==0 or i==H-1 or j==0 or j==W-1) else 0 for j in range(W)] for i in range(H)]
    return res