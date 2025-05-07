from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(sx, sy):
        q = [(sx, sy)]
        seen[sx][sy] = True
        pts = [(sx, sy)]
        color = grid[sx][sy]
        for x, y in q:
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == color:
                    seen[nx][ny] = True
                    q.append((nx, ny))
                    pts.append((nx, ny))
        return pts
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                pts = bfs(i, j)
                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]
                x0, x1 = min(xs), max(xs)
                y0, y1 = min(ys), max(ys)
                # border
                border = set(pts)
                area = (x1-x0+1)*(y1-y0+1)
                if len(pts) < area:
                    # fill interior if hole too big
                    for x in range(x0+1, x1):
                        for y in range(y0+1, y1):
                            if out[x][y] == 0:
                                out[x][y] = grid[i][j]
                else:
                    # erase interior if too full
                    for x in range(x0+1, x1):
                        for y in range(y0+1, y1):
                            if out[x][y] == grid[i][j]:
                                out[x][y] = 0
    return out