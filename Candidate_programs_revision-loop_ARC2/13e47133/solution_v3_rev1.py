from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    # find vertical bar
    vcol = None
    for c in range(w):
        cnt = {}
        for r in range(h):
            cnt[grid[r][c]] = cnt.get(grid[r][c], 0) + 1
        mv, mc = max(cnt.items(), key=lambda x: x[1])
        if mc > h // 2:
            vcol = c
            bar_color = mv
            break
    # find horizontal bars
    bar_rows = [r for r in range(h) if grid[r][vcol] == bar_color]
    bar_rows.sort()
    bands = []
    prev = -1
    for r in bar_rows:
        if r - prev > 1:
            bands.append((prev+1, r-1))
        prev = r
    if prev < h-1:
        bands.append((prev+1, h-1))
    out = [row[:] for row in grid]
    # build pattern for band0, left and right
    def build_pat(r0, r1, c0, c1):
        H = r1 - r0 + 1
        W = c1 - c0 + 1
        vals = {}
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                v = grid[r][c]
                if v != bar_color:
                    vals[v] = vals.get(v,0)+1
        if not vals:
            return [], None
        bg = max(vals.items(), key=lambda x: x[1])[0]
        seeds = []
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                v = grid[r][c]
                if v != bar_color and v != bg:
                    seeds.append((r, c, v))
        primary = None
        if seeds:
            primary = min(seeds, key=lambda x: (x[0]+x[1], x[2]))
        pv = primary[2] if primary else bg
        pat = [[pv]*W for _ in range(H)]
        # draw secondary line(s)
        for r, c, v in seeds:
            if (r, c, v) == primary: continue
            rr = r - r0
            cc = c - c0
            for x in range(1, W-1):
                pat[rr][x] = v
            for y in range(1, H-1):
                pat[y][cc] = v
            mc = W-1-cc
            if mc != cc:
                for y in range(1, H-1):
                    pat[y][mc] = v
            pat[rr][cc] = v
        return pat, (primary[0]-r0, primary[1]-c0) if primary else None
    r0, r1 = bands[0]
    left_pat, left_seed = build_pat(r0, r1, 0, vcol-1)
    right_pat, right_seed = build_pat(r0, r1, vcol+1, w-1)
    # fill band0
    for r in range(r0, r1+1):
        if left_pat:
            for c in range(0, vcol):
                out[r][c] = left_pat[r-r0][c]
        if right_pat:
            for c in range(vcol+1, w):
                out[r][c] = right_pat[r-r0][c-(vcol+1)]
    # propagate to other bands
    nb = len(bands)
    H0 = r1 - r0 + 1
    for i in range(1, nb):
        rr0, rr1 = bands[i]
        Hn = rr1 - rr0 + 1
        # non-last
        if i < nb-1:
            if left_pat:
                rowL = left_pat[H0//2]
                for r in range(rr0, rr1+1):
                    for c in range(0, vcol):
                        out[r][c] = rowL[c]
            if right_pat:
                rowR = right_pat[H0//2]
                for r in range(rr0, rr1+1):
                    for c in range(vcol+1, w):
                        out[r][c] = rowR[c-(vcol+1)]
        else:
            # last band
            if left_pat:
                for k in range(Hn):
                    src = Hn-1-k
                    src = min(src, H0-1)
                    rowL = left_pat[src]
                    for c in range(0, vcol):
                        out[rr0+k][c] = rowL[c]
            if right_pat:
                for k in range(Hn):
                    src = Hn-1-k
                    src = min(src, H0-1)
                    rowR = right_pat[src]
                    for c in range(vcol+1, w):
                        out[rr0+k][c] = rowR[c-(vcol+1)]
    return out