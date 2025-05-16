import numpy as np

def solve(grid):
    m, n = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    seps = [j for j in range(n) if all(grid[i][j] == grid[0][j] != bg for i in range(m))]
    bounds = [-1] + seps + [n]
    segments = [(bounds[k] + 1, bounds[k+1]) for k in range(len(bounds)-1)]
    segs = [np.array([row[s:e] for row in grid]) for s, e in segments]
    first = segs[0]
    out = np.full_like(first, bg)
    for i in range(m):
        for j in range(first.shape[1]):
            c = first[i, j]
            if c != bg and all(seg[i, j] == c for seg in segs):
                out[i, j] = c
    return out.tolist()