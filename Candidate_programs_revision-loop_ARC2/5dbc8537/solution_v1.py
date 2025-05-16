def solve(grid):
    from collections import Counter
    h, w = len(grid), len(grid[0])
    cnt = Counter(x for row in grid for x in row)
    bg, wall = cnt.most_common(1)[0][0], None
    for c, _ in cnt.most_common():
        if c != bg:
            wall = c
            break
    others = set(cnt) - {bg, wall}
    rows = [i for i in range(h) if any(grid[i][j] in others for j in range(w))]
    cols = [j for j in range(w) if any(grid[i][j] in others for i in range(h))]
    if not rows or not cols:
        return [[wall]*w for _ in range(h)]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    if (r1 - r0) >= (c1 - c0):
        sub = grid
        rlo, rhi = r0, r1
        clo, chi = 0, w-1
    else:
        sub = [row[c0:c1+1] for row in grid]
        rlo, rhi = 0, h-1
        clo, chi = c0, c1
    out = []
    for i in range(rlo, rhi+1):
        row = sub[i] if sub is grid else sub[i]
        new = []
        for j in range(clo, chi+1):
            v = grid[i][j] if sub is grid else row[j-clo]
            new.append(v if v in others or v == wall else wall)
        out.append(new)
    return out