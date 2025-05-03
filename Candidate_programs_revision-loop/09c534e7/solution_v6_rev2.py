from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not vis[i][j]:
                queue = deque([(i,j)])
                comp = []
                vis[i][j] = True
                while queue:
                    r, c = queue.popleft()
                    comp.append((r,c))
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 1 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            queue.append((nr,nc))
                minr = min(r for r,c in comp)
                maxr = max(r for r,c in comp)
                minc = min(c for r,c in comp)
                maxc = max(c for r,c in comp)
                if maxr - minr < 2 or maxc - minc < 2:
                    continue
                free = [[False]*(maxc-minc+1) for _ in range(maxr-minr+1)]
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        if grid[r][c] != 1:
                            free[r-minr][c-minc] = True
                visited_bg = [[False]*(maxc-minc+1) for _ in range(maxr-minr+1)]
                dq = deque()
                for c in range(minc, maxc+1):
                    if free[0][c-minc]:
                        dq.append((minr, c))
                        visited_bg[0][c-minc] = True
                    if free[maxr-minr][c-minc]:
                        dq.append((maxr, c))
                        visited_bg[maxr-minr][c-minc] = True
                for r in range(minr, maxr+1):
                    if free[r-minr][0]:
                        dq.append((r, minc))
                        visited_bg[r-minr][0] = True
                    if free[r-minr][maxc-minc]:
                        dq.append((r, maxc))
                        visited_bg[r-minr][maxc-minc] = True
                while dq:
                    r, c = dq.popleft()
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if minr <= nr <= maxr and minc <= nc <= maxc:
                            rr, cc = nr-minr, nc-minc
                            if free[rr][cc] and not visited_bg[rr][cc]:
                                visited_bg[rr][cc] = True
                                dq.append((nr, nc))
                colors = set()
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        rr, cc = r-minr, c-minc
                        if free[rr][cc] and not visited_bg[rr][cc] and grid[r][c] > 1:
                            colors.add(grid[r][c])
                if not colors:
                    continue
                color = next(iter(colors))
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        rr, cc = r-minr, c-minc
                        if free[rr][cc] and not visited_bg[rr][cc] and grid[r][c] == 0:
                            out[r][c] = color
    return out