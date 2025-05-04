from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1 and not visited[r][c]:
                q = deque([(r,c)])
                visited[r][c] = True
                comp = []
                while q:
                    rr, cc = q.popleft()
                    comp.append((rr,cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                rmin, rmax, cmin, cmax = min(rs), max(rs), min(cs), max(cs)
                size_r = rmax - rmin + 1
                size_c = cmax - cmin + 1
                if size_r != size_c or size_r < 3:
                    continue
                size = size_r
                ok = True
                for i in range(size):
                    if grid[rmin][cmin+i] != 1 or grid[rmax][cmin+i] != 1 or grid[rmin+i][cmin] != 1 or grid[rmin+i][cmax] != 1:
                        ok = False
                        break
                if not ok:
                    continue
                marker = None
                for ir in range(rmin+1, rmax):
                    for ic in range(cmin+1, cmax):
                        v = grid[ir][ic]
                        if v not in (0,1):
                            marker = v
                            break
                    if marker is not None:
                        break
                if marker is None:
                    continue
                for ir in range(rmin+1, rmax):
                    for ic in range(cmin+1, cmax):
                        if out[ir][ic] == 0:
                            out[ir][ic] = marker
    return out