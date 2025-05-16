def solve(grid):
    from collections import Counter
    h, w = len(grid), len(grid[0])
    counts = Counter(cell for row in grid for cell in row if cell != 0)
    shape_colors = [c for c, _ in counts.most_common(4)]
    comps = []
    for color in shape_colors:
        rmin, rmax, cmin, cmax = h, -1, w, -1
        for r in range(h):
            for c in range(w):
                if grid[r][c] == color:
                    rmin = min(rmin, r); rmax = max(rmax, r)
                    cmin = min(cmin, c); cmax = max(cmax, c)
        sub = [row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
        def trim(s):
            while True:
                removed = False
                if s and sum(x == color for x in s[0]) <= 1:
                    s = s[1:]; removed = True
                if s and sum(x == color for x in s[-1]) <= 1:
                    s = s[:-1]; removed = True
                if s and s[0] and sum(row[0] == color for row in s) <= 1:
                    s = [row[1:] for row in s]; removed = True
                if s and s[0] and sum(row[-1] == color for row in s) <= 1:
                    s = [row[:-1] for row in s]; removed = True
                if not removed:
                    break
            return s
        sub = trim(sub)
        comps.append((rmin, cmin, color, sub))
    comps.sort(key=lambda x: (x[0], x[1]))
    TL, TR, BL, BR = comps
    subs = [TL[3], TR[3], BL[3], BR[3]]
    th = min(len(s) for s in subs)
    tw = min(len(s[0]) for s in subs)
    TL = [row[:tw] for row in TL[3][:th]]
    TR = [row[:tw] for row in TR[3][:th]]
    BL = [row[:tw] for row in BL[3][:th]]
    BR = [row[:tw] for row in BR[3][:th]]
    out = []
    for r in range(th):
        out.append(TL[r] + TR[r])
    for r in range(th):
        out.append(BL[r] + BR[r])
    return out