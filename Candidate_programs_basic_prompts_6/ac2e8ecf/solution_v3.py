def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                comp = []
                seen[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == color:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
                xs = [p[0] for p in comp]
                ys = [p[1] for p in comp]
                comps.append({
                    "cells": comp,
                    "color": color,
                    "r0": min(xs),
                    "r1": max(xs),
                    "c0": min(ys),
                    "c1": max(ys),
                })
    # detect row-blocks
    blocks = {}
    for k, C in enumerate(comps):
        r0, r1 = C["r0"], C["r1"]
        blocks.setdefault((r0//3), []).append(k)
    blk_keys = sorted(blocks.keys())
    order = []
    if len(blk_keys) == 2:
        order = [blocks[blk_keys[1]], blocks[blk_keys[0]]]
    else:
        if h > 10:
            order = [blocks[blk_keys[1]], blocks[blk_keys[0]], blocks[blk_keys[2]]]
        else:
            order = [blocks[blk_keys[0]], blocks[blk_keys[2]], blocks[blk_keys[1]]]
    new = [[0]*w for _ in range(h)]
    for bi, grp in enumerate(order):
        # compute target top row
        heights = [comps[k]["r1"]-comps[k]["r0"]+1 for k in grp]
        mh = max(heights)
        if len(order) == 2:
            top = 0 if bi == 0 else h-mh
        else:
            if bi == 0:
                top = 0
            elif bi == 1:
                top = heights[0]
            else:
                top = h-mh
        for k in grp:
            C = comps[k]
            dr = top - C["r0"]
            for (x, y) in C["cells"]:
                nx, ny = x+dr, y
                new[nx][ny] = C["color"]
    return new