def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    ccs = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] in (1,8):
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                cnt8 = 0
                minr, maxr, minc, maxc = i, i, j, j
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    if grid[r][c]==8: cnt8 += 1
                    minr = min(minr, r); maxr = max(maxr, r)
                    minc = min(minc, c); maxc = max(maxc, c)
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] in (1,8):
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                if cnt8 <= 1:
                    height = maxr-minr+1
                    ccs.append({
                        "cells": cells,
                        "minr": minr, "minc": minc,
                        "maxr": maxr, "maxc": maxc,
                        "height": height
                    })
    # group by height
    groups = {}
    for cc in ccs:
        groups.setdefault(cc["height"], []).append(cc)
    # sort heights desc
    heights = sorted(groups.keys(), reverse=True)
    # sort each group by maxc desc, then minr asc
    for h0 in heights:
        groups[h0].sort(key=lambda cc: (-cc["maxc"], cc["minr"]))
    selected = []
    used = set()
    # first pass: one per height
    for h0 in heights:
        if len(selected) >= 3: break
        if groups[h0]:
            cc = groups[h0][0]
            selected.append(cc)
            used.add(id(cc))
    # second pass: fill up to 3
    if len(selected) < 3:
        for h0 in heights:
            for cc in groups[h0]:
                if len(selected) >= 3: break
                if id(cc) not in used:
                    selected.append(cc)
                    used.add(id(cc))
            if len(selected) >= 3: break
    # build output
    out = [[0]*w for _ in range(h)]
    for cc in selected:
        for r,c in cc["cells"]:
            out[r][c] = grid[r][c]
    return out