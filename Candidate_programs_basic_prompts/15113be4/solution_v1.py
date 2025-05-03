def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [r for r in range(h) if all(c == grid[r][0] for c in grid[r])]
    sep_cols = [c for c in range(w) if all(grid[r][c] == grid[0][c] for r in range(h))]
    rows = []
    prev = 0
    for r in sep_rows + [h]:
        if r > prev:
            rows.append((prev, r))
        prev = r + 1
    cols = []
    prev = 0
    for c in sep_cols + [w]:
        if c > prev:
            cols.append((prev, c))
        prev = c + 1
    blocks = []
    for br, (rs, re) in enumerate(rows):
        for bc, (cs, ce) in enumerate(cols):
            blocks.append((br, bc, rs, re, cs, ce))
    # find template block (most 8s or most 6s or most 3s)
    from collections import Counter
    cnt = Counter()
    for _, _, rs, re, cs, ce in blocks:
        for r in range(rs, re):
            for c in range(cs, ce):
                if grid[r][c] not in (0,1,4):
                    cnt[(rs,cs,grid[r][c])] += 1
    tmpl_rs, tmpl_cs, marker = max(cnt, key=cnt.get)
    offs = [(r-tmpl_rs, c-tmpl_cs) for r in range(tmpl_rs, tmpl_rs+re-rs) 
            for c in range(tmpl_cs, tmpl_cs+ce-cs) if 0<=r< h and 0<=c<w and grid[r][c]==marker]
    out = [row[:] for row in grid]
    for br, bc, rs, re, cs, ce in blocks:
        if (rs,cs) == (tmpl_rs, tmpl_cs): continue
        for dr, dc in offs:
            r, c = rs+dr, cs+dc
            if 0 <= r < h and 0 <= c < w and grid[r][c] == 1:
                out[r][c] = marker
    return out