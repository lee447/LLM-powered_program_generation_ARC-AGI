from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    freq = {}
    for r in grid:
        for v in r:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=freq.get)
    stripe_cols = []
    for c in range(W):
        col = [grid[r][c] for r in range(H)]
        if bg not in set(col):
            stripe_cols.append(c)
    non_stripe = [c for c in range(W) if c not in stripe_cols]
    band_rows = []
    band_colors = []
    seen = set()
    for r in range(H):
        vs = [grid[r][c] for c in non_stripe]
        if vs and all(v == vs[0] for v in vs) and vs[0] != bg and vs[0] not in seen:
            seen.add(vs[0])
            band_rows.append(r)
            band_colors.append(vs[0])
    stripe_colors = [grid[0][c] for c in stripe_cols]
    sc = len(stripe_cols)
    cols_out = 2*sc + 1
    stripe_pos = [2*i+1 for i in range(sc)]
    out = []
    m = len(band_rows)
    seq = [("spacer", None)]
    for i in range(m):
        seq.append(("band", i))
        seq.append(("spacer", None))
    for typ, idx in seq:
        if typ == "spacer":
            row = [bg] * cols_out
            for j, p in enumerate(stripe_pos):
                row[p] = stripe_colors[j]
        else:
            row = [band_colors[idx]] * cols_out
            r0 = band_rows[idx]
            for j, p in enumerate(stripe_pos):
                row[p] = grid[r0][stripe_cols[j]]
        out.append(row)
    return out