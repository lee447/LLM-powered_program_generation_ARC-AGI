from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    sep_rows = [r for r in range(rows) if grid[r][0] != 0 and all(grid[r][c] == grid[r][0] for c in range(cols))]
    sep_cols = [c for c in range(cols) if grid[0][c] != 0 and all(grid[r][c] == grid[0][c] for r in range(rows))]
    def spans(n, seps):
        seps = sorted(seps)
        spans = []
        prev = 0
        for s in seps:
            if prev < s:
                spans.append((prev, s))
            prev = s + 1
        if prev < n:
            spans.append((prev, n))
        return spans
    brs = spans(rows, sep_rows)
    bcs = spans(cols, sep_cols)
    sep_val = grid[sep_rows[0]][0] if sep_rows else None
    block = []
    for rs, re in brs:
        rowv = []
        for cs, ce in bcs:
            vals = {grid[r][c] for r in range(rs, re) for c in range(cs, ce) if grid[r][c] != 0}
            rowv.append(next(iter(vals)) if vals else 0)
        block.append(rowv)
    cnt = {}
    for r in block:
        for v in r:
            if v and v != sep_val:
                cnt[v] = cnt.get(v, 0) + 1
    colors = [c for c, _ in sorted(cnt.items(), key=lambda x: (x[1], x[0]))]
    h = len(colors)
    w = max(cnt.values()) if cnt else 0
    out = [[0] * w for _ in range(h)]
    for i, c in enumerate(colors):
        for j in range(cnt[c]):
            out[i][j] = c
    return out