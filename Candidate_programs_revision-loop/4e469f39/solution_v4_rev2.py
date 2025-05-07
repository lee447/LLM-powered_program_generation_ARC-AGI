from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    boxes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not vis[i][j]:
                sr = er = i
                sc = ec = j
                stack = [(i, j)]
                vis[i][j] = True
                for x, y in stack:
                    sr = min(sr, x)
                    er = max(er, x)
                    sc = min(sc, y)
                    ec = max(ec, y)
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == 5:
                            vis[nx][ny] = True
                            stack.append((nx, ny))
                boxes.append((sr, er, sc, ec))
    out = [row[:] for row in grid]
    for sr, er, sc, ec in boxes:
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if out[i][j] == 0:
                    out[i][j] = 2
    return out