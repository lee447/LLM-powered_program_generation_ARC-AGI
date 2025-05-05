from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    rows = list(range(R))
    cols = list(range(C))
    h = [i for i in rows if len(set(grid[i]))==1 and grid[i][0]!=0]
    v = [j for j in cols if len({grid[i][j] for i in rows})==1 and grid[0][j]!=0]
    h.sort()
    v.sort()
    row_segments = []
    prev = -1
    for r in h:
        if prev+1 <= r-1:
            row_segments.append((prev+1, r-1))
        prev = r
    if prev+1 <= R-1:
        row_segments.append((prev+1, R-1))
    col_segments = []
    prev = -1
    for c in v:
        if prev+1 <= c-1:
            col_segments.append((prev+1, c-1))
        prev = c
    if prev+1 <= C-1:
        col_segments.append((prev+1, C-1))
    interior_rows = list(range(1, len(row_segments)-1))
    interior_cols = list(range(1, len(col_segments)-1))
    if not interior_rows or not interior_cols:
        return grid
    sep_color = grid[h[0]][h[0]<C and 0 or 0]
    colors = set(sum(grid, [])) - {0, sep_color}
    out = [row[:] for row in grid]
    row_starts = [s for s,e in row_segments]
    col_starts = [s for s,e in col_segments]
    for color in colors:
        pos = [(r,c) for r in rows for c in cols if grid[r][c]==color]
        if not pos:
            continue
        br0 = min(r for r,c in pos)
        br1 = max(r for r,c in pos)
        bc0 = min(c for r,c in pos)
        bc1 = max(c for r,c in pos)
        prs = [i for i,(s,e) in enumerate(row_segments) if not (br1 < s or br0 > e)]
        pcs = [j for j,(s,e) in enumerate(col_segments) if not (bc1 < s or bc0 > e)]
        if not prs or not pcs:
            continue
        len_pr = len(prs)
        len_pc = len(pcs)
        offsets = [(r-br0, c-bc0) for r,c in pos]
        step_r = row_starts[prs[0]+len_pr] - row_starts[prs[0]] if prs[0]+len_pr < len(row_starts) else None
        step_c = col_starts[pcs[0]+len_pc] - col_starts[pcs[0]] if pcs[0]+len_pc < len(col_starts) else None
        drs = []
        if step_r is not None:
            max_vert = len(interior_rows) // len_pr
            for d in range(1, max_vert):
                shifted = [i + d*len_pr for i in prs]
                if all(i in interior_rows for i in shifted):
                    drs.append(d)
        dcs = []
        if step_c is not None:
            max_horiz = len(interior_cols) // len_pc
            for d in range(1, max_horiz):
                shifted = [j + d*len_pc for j in pcs]
                if all(j in interior_cols for j in shifted):
                    dcs.append(d)
        if not drs and not dcs:
            continue
        for d in (drs or [0]):
            for dd in (dcs or [0]):
                if d==0 and dd==0:
                    continue
                for dr,dc in offsets:
                    r0 = br0 + dr + (step_r * d if d>0 else 0)
                    c0 = bc0 + dc + (step_c * dd if dd>0 else 0)
                    out[r0][c0] = color
    return out