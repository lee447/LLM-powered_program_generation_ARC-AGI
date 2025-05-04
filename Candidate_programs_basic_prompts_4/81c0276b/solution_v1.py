from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r, c = len(grid), len(grid[0])
    stripe_rows = {i for i in range(r) if len(set(grid[i])) == 1 and grid[i][0] != 0}
    stripecolor = next(grid[i][0] for i in stripe_rows)
    stripe_cols = {j for j in range(c) if len({grid[i][j] for i in range(r)}) == 1 and grid[0][j] != 0}
    row_segs = []
    cur = []
    for i in range(r):
        if i not in stripe_rows:
            cur.append(i)
        else:
            if cur:
                row_segs.append(cur)
                cur = []
    if cur:
        row_segs.append(cur)
    col_segs = []
    cur = []
    for j in range(c):
        if j not in stripe_cols:
            cur.append(j)
        else:
            if cur:
                col_segs.append(cur)
                cur = []
    if cur:
        col_segs.append(cur)
    row_segs = [seg for seg in row_segs if len(seg) >= 2]
    col_segs = [seg for seg in col_segs if len(seg) >= 2]
    clusters = []
    for seg in row_segs:
        row = []
        for segc in col_segs:
            cnt = {}
            for i in seg:
                for j in segc:
                    v = grid[i][j]
                    if v != 0 and v != stripecolor:
                        cnt[v] = cnt.get(v, 0) + 1
            if cnt:
                color = max(cnt, key=cnt.get)
            else:
                color = 0
            row.append(color)
        clusters.append(row)
    flat = [v for row in clusters for v in row if v != 0]
    from collections import Counter
    counts = Counter(flat)
    colors = sorted(counts, key=lambda x: counts[x])
    ncols = len(col_segs)
    out = []
    for col in colors:
        cnt = counts[col]
        m = min(cnt, ncols)
        out.append([col] * m + [0] * (ncols - m))
    return out