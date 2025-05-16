from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rings = []
    for i in range(h-2):
        for j in range(w-2):
            b = grid[i][j]
            if b == 0: continue
            ok = True
            for di in range(3):
                for dj in range(3):
                    if di == 1 and dj == 1:
                        if grid[i+di][j+dj] == b: ok = False
                    else:
                        if grid[i+di][j+dj] != b: ok = False
            if ok:
                rings.append((i, j, b, grid[i+1][j+1]))
    if not rings:
        return [row[:] for row in grid]
    cols = sorted({j for _, j, *_ in rings})
    rows = sorted({i for i, _, *_ in rings})
    out = [row[:] for row in grid]
    for i, j, b, c in rings:
        for di in range(3):
            for dj in range(3):
                out[i+di][j+dj] = 0
    # rectangle 2x2 case
    if len(rings) == 4 and len(cols) == 2 and len(rows) == 2:
        r1, r2 = rows[0], rows[1]
        c1, c2 = cols[0], cols[1]
        mp = {(i,j):(b,c) for i,j,b,c in rings}
        b11, c11 = mp[(r1,c1)]
        b12, c12 = mp[(r1,c2)]
        b21, c21 = mp[(r2,c1)]
        b22, c22 = mp[(r2,c2)]
        # keep (r1,c1) and (r2,c2)
        for (ri, cj, bb, cc), newc in [((r1,c1,b11,c11), c21), ((r2,c2,b22,c22), c12)]:
            for di in (0,1,2):
                for dj in (0,2):
                    out[ri+di][cj+dj] = bb
            for dj in (0,1,2):
                for di in (0,2):
                    out[ri+di][cj+dj] = bb
            out[ri+1][cj+1] = newc
        return out
    # two-column case
    if len(cols) == 2:
        cL, cR = cols[0], cols[1]
        left = sorted([r for r in rings if r[1] == cL], key=lambda x: x[0])
        right = sorted([r for r in rings if r[1] == cR], key=lambda x: x[0])
        removed_centers = [c for _,_,_,c in left if c != 0]
        for k, (ri, cj, bb, cc) in enumerate(right):
            if k < len(removed_centers):
                newc = removed_centers[k]
                for di in (0,1,2):
                    for dj in (0,2):
                        out[ri+di][cj+dj] = bb
                for dj in (0,1,2):
                    for di in (0,2):
                        out[ri+di][cj+dj] = bb
                out[ri+1][cj+1] = newc
        return out
    # general case >2 columns
    from statistics import mean
    groups = {}
    for r in rings:
        groups.setdefault(r[1], []).append(r)
    avgs = {c: mean([b for _,_,b,_ in lst]) for c,lst in groups.items()}
    keep_col = max(avgs, key=lambda x: avgs[x])
    kept = groups[keep_col]
    center_row = h/2
    kept_ring = min(kept, key=lambda r: abs((r[0]+1) - center_row))
    removed = [r for r in rings if r[1] != keep_col]
    removed_centers = [c for _,_,_,c in sorted(removed, key=lambda x: x[0]) if c != 0]
    newc = removed_centers[0] if removed_centers else kept_ring[3]
    ri, cj, bb, _ = kept_ring
    for di in (0,1,2):
        for dj in (0,2):
            out[ri+di][cj+dj] = bb
    for dj in (0,1,2):
        for di in (0,2):
            out[ri+di][cj+dj] = bb
    out[ri+1][cj+1] = newc
    return out