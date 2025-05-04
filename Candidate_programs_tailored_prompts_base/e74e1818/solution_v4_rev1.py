from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if orig[i][j] != 0 and not visited[i][j]:
                color = orig[i][j]
                q = [(i, j)]
                visited[i][j] = True
                rmin = rmax = i
                cmin = cmax = j
                idx = 0
                while idx < len(q):
                    x, y = q[idx]; idx += 1
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and orig[nx][ny] == color:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            rmin = min(rmin, nx)
                            rmax = max(rmax, nx)
                            cmin = min(cmin, ny)
                            cmax = max(cmax, ny)
                bh = rmax - rmin + 1
                bw = cmax - cmin + 1
                sub = [orig[rmin+rr][cmin:cmin+bw] for rr in range(bh)]
                rev = [row[::-1] for row in sub[::-1]]
                for rr in range(bh):
                    for cc in range(bw):
                        res[rmin+rr][cmin+cc] = rev[rr][cc]
    return res