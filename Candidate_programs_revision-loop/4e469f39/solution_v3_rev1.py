from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    boxes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not vis[i][j]:
                q = [(i, j)]
                vis[i][j] = True
                sr = er = i
                sc = ec = j
                for x, y in q:
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == 5:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                            sr = min(sr, nx)
                            er = max(er, nx)
                            sc = min(sc, ny)
                            ec = max(ec, ny)
                boxes.append((sr, er, sc, ec))
    out = [row[:] for row in grid]
    for sr, er, sc, ec in boxes:
        for i in range(sr+1, er):
            for j in range(sc+1, ec):
                if out[i][j] == 0:
                    out[i][j] = 2
        for j in range(sc, ec+1):
            if out[sr][j] == 0:
                out[sr][j] = 2
            if out[er][j] == 0:
                out[er][j] = 2
        for i in range(sr, er+1):
            if out[i][sc] == 0:
                out[i][sc] = 2
            if out[i][ec] == 0:
                out[i][ec] = 2
    return out