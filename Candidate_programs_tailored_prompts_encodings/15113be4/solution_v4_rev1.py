from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sepR = [i for i in range(h) if all(c == 4 for c in grid[i])]
    sepC = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    subRs = [(0, sepR[0]-1)] + [(sepR[i]+1, sepR[i+1]-1) for i in range(len(sepR)-1)] + [(sepR[-1]+1, h-1)]
    subRs = [(r0, r1) for r0, r1 in subRs if r0 <= r1]
    subCs = [(0, sepC[0]-1)] + [(sepC[i]+1, sepC[i+1]-1) for i in range(len(sepC)-1)] + [(sepC[-1]+1, w-1)]
    subCs = [(c0, c1) for c0, c1 in subCs if c0 <= c1]
    orig = grid
    out = [row[:] for row in grid]
    regionVals = {}
    for i, (r0, r1) in enumerate(subRs):
        for j, (c0, c1) in enumerate(subCs):
            vals = {orig[r][c] for r in range(r0, r1+1) for c in range(c0, c1+1) if orig[r][c] not in (0,1,4)}
            regionVals[(i,j)] = vals
    visited = [[False]*w for _ in range(h)]
    for i, (r0, r1) in enumerate(subRs):
        for j, (c0, c1) in enumerate(subCs):
            if not regionVals[(i,j)]: continue
            val = next(iter(regionVals[(i,j)]))
            # find clusters of this val in region
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if orig[r][c] == val and not visited[r][c]:
                        # BFS cluster
                        q = deque([(r,c)])
                        cluster = []
                        visited[r][c] = True
                        while q:
                            rr, cc = q.popleft()
                            cluster.append((rr, cc))
                            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                                nr, nc = rr+dr, cc+dc
                                if r0 <= nr <= r1 and c0 <= nc <= c1 and not visited[nr][nc] and orig[nr][nc]==val:
                                    visited[nr][nc] = True
                                    q.append((nr,nc))
                        # bounding box of cluster
                        minr = min(rr for rr,cc in cluster)
                        maxr = max(rr for rr,cc in cluster)
                        minc = min(cc for rr,cc in cluster)
                        maxc = max(cc for rr,cc in cluster)
                        h0 = r1-r0+1; w0 = c1-c0+1
                        shape_h = maxr-minr+1; shape_w = maxc-minc+1
                        r_rel = minr - r0
                        c_rel = minc - c0
                        # try horizontal
                        if j+1 < len(subCs):
                            w1 = subCs[j+1][1]-subCs[j+1][0]+1
                            step = w0//w1 if w1>0 else 1
                            j2 = j+step
                            if j2 < len(subCs) and not regionVals.get((i,j2)):
                                tr0, tr1 = subRs[i]
                                tc0, tc1 = subCs[j2]
                                left = c_rel*2 < w0
                                top = r_rel*2 < h0
                                new_minr = tr0 + (0 if top else (tr1-tr0+1-shape_h))
                                new_minc = tc0 + (0 if left else (tc1-tc0+1-shape_w))
                                for rr, cc in cluster:
                                    dr = rr - minr
                                    dc = cc - minc
                                    nr = new_minr + dr
                                    nc = new_minc + dc
                                    if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == 1:
                                        out[nr][nc] = val
                                continue
                        # try vertical
                        if i+1 < len(subRs):
                            h1 = subRs[i+1][1]-subRs[i+1][0]+1
                            step = h0//h1 if h1>0 else 1
                            i2 = i+step
                            if i2 < len(subRs) and not regionVals.get((i2,j)):
                                tr0, tr1 = subRs[i2]
                                tc0, tc1 = subCs[j]
                                left = c_rel*2 < w0
                                top = r_rel*2 < h0
                                new_minr = tr0 + (0 if top else (tr1-tr0+1-shape_h))
                                new_minc = tc0 + (0 if left else (tc1-tc0+1-shape_w))
                                for rr, cc in cluster:
                                    dr = rr - minr
                                    dc = cc - minc
                                    nr = new_minr + dr
                                    nc = new_minc + dc
                                    if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == 1:
                                        out[nr][nc] = val
    return out