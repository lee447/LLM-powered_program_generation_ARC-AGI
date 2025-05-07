import itertools

def solve(grid):
    h, w = len(grid), len(grid[0])
    shape0 = [(0,2),(0,3),(1,0),(1,1),(2,2)]
    variants = []
    mirrors = [shape0, [(r,-c) for r,c in shape0]]
    for base in mirrors:
        for k in range(4):
            pts = base
            for _ in range(k):
                pts = [(c, -r) for r,c in pts]
            minr = min(r for r,c in pts)
            minc = min(c for r,c in pts)
            norm = sorted([(r-minr, c-minc) for r,c in pts])
            if norm not in variants:
                variants.append(norm)
    out = [row[:] for row in grid]
    clusters = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 1:
                clusters.setdefault(c, []).append((i,j))
    for c, pts in clusters.items():
        for rel in variants:
            if len(pts) > len(rel):
                continue
            found = False
            rel_set = set(rel)
            for pi, pj in pts:
                for r0 in rel:
                    oi = pi - r0[0]
                    oj = pj - r0[1]
                    if oi < 0 or oj < 0:
                        continue
                    if oi + max(r for r,c2 in rel) >= h or oj + max(c2 for r,c2 in rel) >= w:
                        continue
                    ok = True
                    for qi, qj in pts:
                        if (qi-oi, qj-oj) not in rel_set:
                            ok = False
                            break
                    if not ok:
                        continue
                    for dr, dc in rel:
                        out[oi+dr][oj+dc] = c
                    found = True
                    break
                if found:
                    break
            if found:
                break
    return out