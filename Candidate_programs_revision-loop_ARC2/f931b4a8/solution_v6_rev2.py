from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    h2, w2 = H // 2, W // 2
    quads = {
        'TL': [row[:w2] for row in grid[:h2]],
        'TR': [row[w2:] for row in grid[:h2]],
        'BL': [row[:w2] for row in grid[h2:]],
        'BR': [row[w2:] for row in grid[h2:]]
    }
    def uniq(a):
        s = set()
        for r in a:
            s |= set(r)
        return s
    def nonzero(a):
        return {x for x in uniq(a) if x != 0}
    def has_zero(a):
        return any(0 in r for r in a)
    # find fill quad: most colors (>=2)
    fill_name = max(quads, key=lambda n: len(nonzero(quads[n])))
    if len(nonzero(quads[fill_name])) < 2:
        fill_name = max(quads, key=lambda n: len(uniq(quads[n])) - (has_zero(quads[n]) and 1 or 0))
    fill = quads[fill_name]
    # find mask quad: one color + holes, not the fill quad
    mask_name = next(n for n in quads if n != fill_name and len(nonzero(quads[n])) == 1 and has_zero(quads[n]))
    mask = quads[mask_name]
    mask_color = next(iter(nonzero(mask)))
    # period finder
    def period(a):
        h, w = len(a), len(a[0])
        for ph in range(1, h+1):
            if h % ph == 0 and all(a[i] == a[i % ph] for i in range(h)):
                break
        for pw in range(1, w+1):
            if w % pw == 0 and all(a[i][j] == a[i][j % pw] for i in range(h) for j in range(w)):
                break
        return ph, pw
    ph_f, pw_f = period(fill)
    ph_m, pw_m = period(mask)
    # unify period
    th = ph_f * ph_m // math.gcd(ph_f, ph_m)
    tw = pw_f * pw_m // math.gcd(pw_f, pw_m)
    # build tile
    tile = [[0]*tw for _ in range(th)]
    for i in range(th):
        for j in range(tw):
            if mask[i % ph_m][j % pw_m] != 0:
                tile[i][j] = mask_color
            else:
                tile[i][j] = fill[i % ph_f][j % pw_f]
    # tile out to cover both mask and fill extents
    # determine how many repeats
    # use the extents of zeros in mask quad to decide cropping
    out_h = (h2 // ph_m or 1) * th
    out_w = (w2 // pw_m or 1) * tw
    out_h *= (len(nonzero(quads['TL'])) > 0) + (len(nonzero(quads['BL'])) > 0)
    out_w *= (len(nonzero(quads['TL'])) > 0) + (len(nonzero(quads['TR'])) > 0)
    if out_h == 0: out_h = th
    if out_w == 0: out_w = tw
    res = [[tile[i % th][j % tw] for j in range(out_w)] for i in range(out_h)]
    return res