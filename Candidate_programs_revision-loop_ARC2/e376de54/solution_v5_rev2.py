from typing import List
from collections import Counter
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = Counter(v for row in grid for v in row)
    bg = max(cnt, key=cnt.get)
    pts_by_color = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                pts_by_color.setdefault(v, []).append((r, c))
    colors = list(pts_by_color.keys())
    dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]
    # group points by color, dir, pkey
    grouping = {c: {} for c in colors}
    for c in colors:
        for dr, dc in dirs:
            d = {}
            for r, col in pts_by_color[c]:
                p = r*dc - col*dr
                d.setdefault(p, []).append((r, col))
            grouping[c][(dr, dc)] = d
    # pick best_dir
    if len(colors) > 1:
        freq = {}
        for c in colors:
            best = None
            blen = 0
            for dr, dc in dirs:
                for grp in grouping[c][(dr, dc)].values():
                    if len(grp) > blen:
                        blen = len(grp)
                        best = (dr, dc)
            freq[best] = freq.get(best, 0) + 1
        best_dr, best_dc = max(freq, key=freq.get)
    else:
        c = colors[0]
        best_dr, best_dc = next((dr, dc) for dr, dc in dirs
                                 if any(len(g) >= 2 for g in grouping[c][(dr, dc)].values()))
    norm2 = best_dr*best_dr + best_dc*best_dc
    # multi-color
    if len(colors) > 1:
        main = {}
        for c in colors:
            d = grouping[c][(best_dr, best_dc)]
            p, grp = max(d.items(), key=lambda kv: len(kv[1]))
            main[c] = (p, grp)
        lens = sorted({len(grp) for p, grp in main.values()})
        L = lens[-2] if len(lens) > 1 else lens[0]
        # ref start T
        T0 = min(r*best_dr + c0*best_dc for p, grp in main.values() if len(grp) == L for r, c0 in grp)
        out = [[bg]*w for _ in range(h)]
        for c in colors:
            p, _ = main[c]
            for i in range(L):
                T = T0 + i*norm2
                r = (best_dr*T + best_dc*p) // norm2
                cc = (best_dc*T - best_dr*p) // norm2
                if 0 <= r < h and 0 <= cc < w:
                    out[r][cc] = c
        return out
    # single-color
    c = colors[0]
    d = grouping[c][(best_dr, best_dc)]
    valid = [(p, grp) for p, grp in d.items() if len(grp) >= 2]
    lens = sorted({len(grp) for p, grp in valid})
    L = lens[-2] if len(lens) > 1 else lens[0]
    T0 = min(r*best_dr + c0*best_dc for p, grp in valid if len(grp) == L for r, c0 in grp)
    out = [[bg]*w for _ in range(h)]
    for p, grp in valid:
        for i in range(L):
            T = T0 + i*norm2
            r = (best_dr*T + best_dc*p) // norm2
            cc = (best_dc*T - best_dr*p) // norm2
            if 0 <= r < h and 0 <= cc < w:
                out[r][cc] = c
    return out