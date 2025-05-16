from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    rmin, cmin = rows, cols
    rmax = cmax = -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 5:
                rmin = min(rmin, i)
                rmax = max(rmax, i)
                cmin = min(cmin, j)
                cmax = max(cmax, j)
    region = [row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
    H, W = len(region), len(region[0])
    border = region[0][0]
    cnt = {}
    for i in range(H):
        for j in range(W):
            v = region[i][j]
            if v != border:
                cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=cnt.get)
    shape_colors = [v for v in cnt if v != bg]
    cands = sorted(set(range(10)) - {border, bg} - set(shape_colors))
    if cands and cands[0] == 0:
        cands = cands[1:]
    mapping = {shape_colors[i]: cands[i] for i in range(len(shape_colors))}
    res = [list(r) for r in region]
    for i in range(H):
        for j in range(W):
            v = res[i][j]
            if v in mapping:
                res[i][j] = mapping[v]
    if len(shape_colors) == 2:
        interior_rows = list(range(1, H-1))
        interior_cols = list(range(1, W-1))
        shape_rows = [r for r in interior_rows if any(res[r][c] not in {border, bg} for c in interior_cols)]
        shape_cols = [c for c in interior_cols if any(res[r][c] not in {border, bg} for r in interior_rows)]
        def groups(xs):
            segs = []
            cur = []
            for x in xs:
                if not cur or x == cur[-1] + 1:
                    cur.append(x)
                else:
                    segs.append(cur)
                    cur = [x]
            if cur: segs.append(cur)
            return segs
        row_segs = groups(shape_rows)
        col_segs = groups(shape_cols)
        bh = len(row_segs[0])
        bw = len(col_segs[0])
        for seg in row_segs:
            r0 = seg[0]
            for segc in col_segs:
                c0 = segc[0] + bw // 2
                res[r0][c0] = bg
    return res