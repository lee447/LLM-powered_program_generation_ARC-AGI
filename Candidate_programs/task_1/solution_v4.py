import numpy as np
from collections import deque
def solve(grid):
    arr = np.array(grid)
    nrows, ncols = arr.shape
    out = np.zeros_like(arr)
    visited = np.zeros_like(arr, dtype=bool)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(nrows):
        for j in range(ncols):
            if arr[i,j] != 0 and not visited[i,j]:
                col = arr[i,j]
                q = deque()
                q.append((i,j))
                comp = []
                visited[i,j] = True
                while q:
                    r,c = q.popleft()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<nrows and 0<=nc<ncols and not visited[nr,nc] and arr[nr,nc]==col:
                            visited[nr,nc] = True
                            q.append((nr,nc))
                rs = [p[0] for p in comp]
                cs = [p[1] for p in comp]
                rmin, rmax = min(rs), max(rs)
                cmin, cmax = min(cs), max(cs)
                out[rmin:rmax+1, cmin:cmax+1] = col
    return out.tolist()