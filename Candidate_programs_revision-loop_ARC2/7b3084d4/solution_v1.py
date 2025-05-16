def solve(grid):
    from collections import defaultdict
    h, w = len(grid), len(grid[0])
    comps = []
    for color in sorted({grid[r][c] for r in range(h) for c in range(w)}):
        if color == 0: continue
        rmin, rmax, cmin, cmax = h, -1, w, -1
        for r in range(h):
            for c in range(w):
                if grid[r][c] == color:
                    rmin = min(rmin, r); rmax = max(rmax, r)
                    cmin = min(cmin, c); cmax = max(cmax, c)
        sub = [row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
        # trim rows/cols with <=1 non-zero
        def trim(s):
            changed = True
            while changed:
                changed = False
                # top row
                if len(s)>0 and sum(1 for x in s[0] if x!=0) <= 1:
                    s = s[1:]; changed = True
                # bottom row
                if len(s)>0 and sum(1 for x in s[-1] if x!=0) <= 1:
                    s = s[:-1]; changed = True
                # left col
                if s and len(s[0])>0 and sum(1 for row in s if row[0]!=0) <= 1:
                    s = [row[1:] for row in s]; changed = True
                # right col
                if s and len(s[0])>0 and sum(1 for row in s if row[-1]!=0) <= 1:
                    s = [row[:-1] for row in s]; changed = True
            return s
        sub = trim(sub)
        comps.append((rmin, cmin, color, sub))
    comps.sort(key=lambda x: (x[0], x[1]))
    # get quadrants
    TL, TR, BL, BR = comps[0], comps[1], comps[2], comps[3]
    subs = [TL[3], TR[3], BL[3], BR[3]]
    # pad to common size
    max_h = max(s and len(s) for s in subs)
    max_w = max(s and len(s[0]) for s in subs)
    def pad(s, color):
        sh = len(s); sw = len(s[0])
        for row in s:
            row += [color] * (max_w - sw)
        for _ in range(max_h - sh):
            s.append([color] * max_w)
        return s
    TL = pad(subs[0], TL[2])
    TR = pad(subs[1], TR[2])
    BL = pad(subs[2], BL[2])
    BR = pad(subs[3], BR[2])
    out = []
    for r in range(max_h):
        out.append(TL[r] + TR[r])
    for r in range(max_h):
        out.append(BL[r] + BR[r])
    return out