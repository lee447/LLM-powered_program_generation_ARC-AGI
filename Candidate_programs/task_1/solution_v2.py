import numpy as np
from collections import deque

def solve(grid):
    arr = np.array(grid)
    nrows, ncols = arr.shape
    out = np.zeros_like(arr)
    visited = np.zeros_like(arr, dtype=bool)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    def bfs(sr, sc, col):
        q = deque()
        q.append((sr,sc))
        comp = []
        visited[sr,sc] = True
        while q:
            r,c = q.popleft()
            comp.append((r,c))
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<nrows and 0<=nc<ncols:
                    if not visited[nr,nc] and arr[nr,nc]==col:
                        visited[nr,nc] = True
                        q.append((nr,nc))
        return comp

    # Erode a boolean block: for each cell that is True, check all neighbors in its 3x3 (existing ones)
    def erode(block):
        br, bc = block.shape
        er = np.zeros_like(block, dtype=bool)
        for i in range(br):
            for j in range(bc):
                if block[i,j]:
                    ok = True
                    for di in (-1,0,1):
                        for dj in (-1,0,1):
                            ni, nj = i+di, j+dj
                            if 0<=ni<br and 0<=nj<bc:
                                if not block[ni, nj]:
                                    ok = False
                                    break
                        if not ok:
                            break
                    if ok:
                        er[i,j] = True
        return er

    # Process each connected component (4-connected) of nonzero (non-background) cells.
    for i in range(nrows):
        for j in range(ncols):
            if arr[i,j] != 0 and not visited[i,j]:
                col = arr[i,j]
                comp = bfs(i,j,col)
                rs = [p[0] for p in comp]
                cs = [p[1] for p in comp]
                rmin, rmax = min(rs), max(rs)
                cmin, cmax = min(cs), max(cs)
                h = rmax - rmin + 1
                w = cmax - cmin + 1
                comp_mask = np.zeros((h,w), dtype=bool)
                for r,c in comp:
                    comp_mask[r - rmin, c - cmin] = True
                # Decide core: if region is very thin in any direction, use full component
                if h < 3 or w < 3:
                    core = comp_mask.copy()
                else:
                    core = erode(comp_mask)
                    if not core.any():
                        core = comp_mask.copy()
                # Get bounding box of core in local coordinates
                coords = np.argwhere(core)
                if len(coords)==0:
                    core_box = (0,0,0,0)
                    core_h, core_w = 0,0
                else:
                    crmin, ccmin = coords.min(axis=0)
                    crmax, ccmax = coords.max(axis=0) + 1
                    core_h = crmax - crmin
                    core_w = ccmax - ccmin
                # Create a block of size (h,w) with a centered rectangle of size (core_h, core_w)
                block = np.zeros((h,w), dtype=bool)
                start_r = (h - core_h) // 2
                start_c = (w - core_w) // 2
                if core_h > 0 and core_w > 0:
                    block[start_r:start_r+core_h, start_c:start_c+core_w] = True
                # Write the color to output in the bounding box where block==True
                sub = out[rmin:rmax+1, cmin:cmax+1]
                sub[block] = col
                out[rmin:rmax+1, cmin:cmax+1] = sub
    return out.tolist()