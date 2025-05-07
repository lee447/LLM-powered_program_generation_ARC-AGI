from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    r0s = min(r for r in range(R) if any(grid[r][c] == 1 for c in range(C)))
    r1s = max(r for r in range(R) if any(grid[r][c] == 1 for c in range(C)))
    pivots = [(c, grid[r0s-1][c]) for c in range(C) if grid[r0s-1][c] > 1]
    cols = [c for c in range(C) if any(grid[r][c] == 1 for r in range(r0s, r1s+1))]
    clusters = []
    cur = []
    for c in cols:
        if not cur or c == cur[-1] + 1:
            cur.append(c)
        else:
            clusters.append(cur)
            cur = [c]
    if cur: clusters.append(cur)
    templates = {}
    for (_, color), cl in zip(pivots, clusters):
        c0, c1 = cl[0], cl[-1]
        h = r1s - r0s + 1
        w = c1 - c0 + 1
        mask = [[0]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if grid[r0s + i][c0 + j] == 1:
                    mask[i][j] = 1
        templates[color] = (mask, h, w)
    rows5 = [r for r in range(R) if any(grid[r][c] == 5 for c in range(C))]
    rclusters = []
    cur = []
    for r in rows5:
        if not cur or r == cur[-1] + 1:
            cur.append(r)
        else:
            rclusters.append(cur)
            cur = [r]
    if cur: rclusters.append(cur)
    cols5 = [c for c in range(C) if any(grid[r][c] == 5 for r in range(R))]
    cclusters = []
    cur = []
    for c in cols5:
        if not cur or c == cur[-1] + 1:
            cur.append(c)
        else:
            cclusters.append(cur)
            cur = [c]
    if cur: cclusters.append(cur)
    r0f, r1f = rclusters[0][0], rclusters[-1][-1]
    c0f, c1f = cclusters[0][0], cclusters[-1][-1]
    H = r1f - r0f + 1
    W = c1f - c0f + 1
    out = [[0]*W for _ in range(H)]
    for rc in rclusters:
        for cc in cclusters:
            color = None
            for r in rc:
                for c in cc:
                    v = grid[r][c]
                    if v != 5 and v != 0:
                        color = v
            if color is None or color not in templates:
                continue
            mask, h, w = templates[color]
            r0b, c0b = rc[0], cc[0]
            for i in range(h):
                for j in range(w):
                    if mask[i][j]:
                        rr = r0b + i
                        cc2 = c0b + j
                        out[rr - r0f][cc2 - c0f] = color
    return out