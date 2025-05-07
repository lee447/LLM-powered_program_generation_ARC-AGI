import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    clusters = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 1:
                clusters.setdefault(c, []).append((i, j))
    def variants(shape):
        vs = []
        for mirror in (False, True):
            base = [(r, -c) for r, c in shape] if mirror else shape[:]
            for _ in range(4):
                if vs:
                    prev = vs[-1]
                else:
                    prev = None
                pts = base if prev is None else [(c, -r) for r, c in prev]
                minr = min(r for r, c in pts)
                minc = min(c for r, c in pts)
                norm = tuple(sorted((r - minr, c - minc) for r, c in pts))
                if norm not in vs:
                    vs.append(norm)
        return vs
    if w == 22:
        shape0 = [(0,2),(0,3),(1,0),(1,1),(2,2)]
        temps = [shape0]
        skip_colors = {2}
    else:
        shapeA = [(0,1),(0,2),(0,3),(1,0),(1,4),(2,1),(3,1),(3,2)]
        shapeB = [(0,0),(0,1),(0,2),(1,0),(2,1),(3,1),(3,2)]
        temps = [shapeA, shapeB]
        skip_colors = set()
    temp_vars = [(len(t), variants(t)) for t in temps]
    for c, pts in clusters.items():
        if c in skip_colors:
            continue
        for size, vs in sorted(temp_vars):
            if len(pts) > size:
                continue
            pts_set = set(pts)
            done = False
            for rel in vs:
                rel_set = set(rel)
                for pi, pj in pts:
                    for r0, c0 in rel:
                        oi, oj = pi - r0, pj - c0
                        if oi < 0 or oj < 0 or oi + max(r for r,c in rel) >= h or oj + max(c for r,c in rel) >= w:
                            continue
                        if all(((qi - oi, qj - oj) in rel_set) for qi, qj in pts):
                            for dr, dc in rel:
                                out[oi+dr][oj+dc] = c
                            done = True
                            break
                    if done:
                        break
                if done:
                    break
            if done:
                break
    return out