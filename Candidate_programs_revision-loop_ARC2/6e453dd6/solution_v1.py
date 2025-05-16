def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripe = next(c for c in range(w) if any(grid[r][c] == 5 for r in range(h)))
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h):
        for c in range(stripe):
            if grid[r][c] == 0 and not visited[r][c]:
                cells = []
                stack = [(r,c)]
                visited[r][c] = True
                while stack:
                    rr, cc = stack.pop()
                    cells.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<h and 0<=nc<stripe and grid[nr][nc]==0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                ys = [p[0] for p in cells]
                xs = [p[1] for p in cells]
                clusters.append({
                    "cells": cells,
                    "min_r": min(ys),
                    "max_r": max(ys),
                    "min_c": min(xs),
                    "max_c": max(xs),
                })
    clusters.sort(key=lambda x: x["min_r"])
    if not clusters:
        return grid
    mid = len(clusters) // 2
    mc = clusters[mid]
    d = stripe - 1 - mc["max_c"]
    # shift clusters up to mid
    for i in range(mid+1):
        cl = clusters[i]
        for r,c in cl["cells"]:
            grid[r][c] = 6
        for r,c in cl["cells"]:
            grid[r][c+d] = 0
    # fill red for hole‐rows of clusters[1..mid]
    for i in range(1, mid+1):
        cl = clusters[i]
        width = cl["max_c"] - cl["min_c"] + 1
        counts = {}
        for r,c in cl["cells"]:
            counts.setdefault(r,0)
            counts[r] += 1
        for r in range(cl["min_r"], cl["max_r"]+1):
            if counts.get(r,0) < width and counts.get(r,0)>0:
                for cc in range(stripe+1, w):
                    grid[r][cc] = 2
    return grid