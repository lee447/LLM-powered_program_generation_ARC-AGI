from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    bands = []
    i = 0
    while i < h:
        if any(grid[i][j] == 1 for j in range(w)):
            r0 = i
            while i + 1 < h and any(grid[i+1][j] == 1 for j in range(w)):
                i += 1
            r1 = i
            bands.append((r0, r1))
        i += 1
    band_vals = []
    for r0, r1 in bands:
        walls = [c for c in range(w) if all(grid[r][c] == 1 for r in range(r0, r1+1))]
        walls.sort()
        gaps = []
        vals = []
        for k in range(len(walls)-1):
            c0, c1 = walls[k], walls[k+1]
            gaps.append((c0, c1))
            v = grid[r0+1][c0+1]
            vals.append(v if v != grid[0][0] and v != 8 else None)
        for k in range(len(vals)):
            if vals[k] is None:
                d, sel = w*h, None
                for j in range(len(vals)):
                    if vals[j] is not None and abs(j-k) < d:
                        d = abs(j-k); sel = j
                vals[k] = vals[sel]
        band_vals.append((gaps, vals))
        for (c0, c1), v in zip(gaps, vals):
            for r in range(r0+1, r1):
                for c in range(c0+1, c1):
                    out[r][c] = v
    for b in range(len(bands)-1):
        r1 = bands[b][1]
        r2 = bands[b+1][0]
        r0 = r1+1; r3 = r2-1
        if r0>r3: continue
        gaps, vals1 = band_vals[b]
        _, vals2 = band_vals[b+1]
        h2 = r3 - r0 + 1
        if h2 > 1:
            for c0,c1 in (gaps[0], gaps[-1]):
                v = vals1[0] if (c0,c1)==gaps[0] else vals2[-1]
                for r in range(r0, r3+1):
                    for c in range(c0+1, c1):
                        out[r][c] = v
        else:
            for k, (c0,c1) in enumerate(gaps):
                v = vals1[k] if vals1[k] is not None else vals2[k]
                if grid[r0][c0+1] == 8:
                    for c in range(c0+1, c1):
                        out[r0][c] = v
    return out