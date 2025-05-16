from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    h2, w2 = H//2, W//2
    TL = [row[:w2] for row in grid[:h2]]
    TR = [row[w2:] for row in grid[:h2]]
    BL = [row[:w2] for row in grid[h2:]]
    BR = [row[w2:] for row in grid[h2:]]
    def uniq(a):
        s=set()
        for r in a:
            s |= set(r)
        return s
    Qs = [(TL, "TL"), (TR, "TR"), (BL, "BL"), (BR, "BR")]
    mask = fill = None
    for quad, _ in Qs:
        u = uniq(quad)
        if len(u)==2 and 0 in u:
            mask = quad
            break
    if mask is None:
        for quad, _ in Qs:
            u = uniq(quad)
            if len(u)>1:
                mask = quad
                break
    # fill is diagonal
    if mask is TL: fill = BR
    elif mask is TR: fill = BL
    elif mask is BL: fill = TR
    else: fill = TL
    if len(uniq(mask))==1:
        return fill
    # build tile
    cnt = {}
    for r in mask:
        for v in r:
            cnt[v] = cnt.get(v,0)+1
    bg = max(cnt, key=lambda x: cnt[x])
    fvals = uniq(fill) - {0}
    fill_color = next(iter(fvals)) if fvals else 0
    tile = [[fill_color if v==bg else v for v in row] for row in mask]
    fu = uniq(fill) - {0}
    if len(fu)<=1:
        rep_rows, rep_cols = len(fill), 1
    else:
        rep_rows, rep_cols = len(fill), len(fill[0])
    out = []
    th, tw = len(tile), len(tile[0])
    for i in range(rep_rows*th):
        row = []
        for j in range(rep_cols*tw):
            row.append(tile[i%th][j%tw])
        out.append(row)
    return out