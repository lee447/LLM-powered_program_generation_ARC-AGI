from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe = next(c for c in range(w) if any(grid[r][c] == 5 for r in range(h)))
    out = [row[:] for row in grid]
    # find zero‐clusters left of the gray stripe
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h):
        for c in range(stripe):
            if grid[r][c] == 0 and not visited[r][c]:
                stack = [(r, c)]
                visited[r][c] = True
                cells = []
                while stack:
                    rr, cc = stack.pop()
                    cells.append((rr, cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < stripe and grid[nr][nc] == 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                ys = [p[0] for p in cells]
                xs = [p[1] for p in cells]
                clusters.append({
                    "cells": cells,
                    "min_r": min(ys),
                    "max_r": max(ys),
                    "min_c": min(xs),
                    "max_c": max(xs),
                })
    clusters.sort(key=lambda cl: cl["min_r"])
    keep = set()
    n = len(clusters)
    for i, cl in enumerate(clusters):
        wcl = cl["max_c"] - cl["min_c"] + 1
        counts = {}
        for rr, cc in cl["cells"]:
            counts[rr] = counts.get(rr, 0) + 1
        # decide which rows keep their red stripe
        if i == 0 and n % 2 == 1:
            continue
        if wcl == 1:
            for r0 in range(cl["min_r"], cl["max_r"]):
                keep.add(r0)
        else:
            for r0 in range(cl["min_r"], cl["max_r"]):
                if counts.get(r0, 0) < wcl:
                    keep.add(r0)
    for r in range(h):
        for c in range(stripe+1, w):
            if r in keep and grid[r][c] == 2:
                out[r][c] = 2
            else:
                out[r][c] = 6
    return out