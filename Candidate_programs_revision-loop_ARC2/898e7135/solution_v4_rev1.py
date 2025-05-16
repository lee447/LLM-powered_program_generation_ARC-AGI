from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for row in grid:
        for c in row:
            if c != 0:
                cnt[c] = cnt.get(c, 0) + 1
    nonzero = list(cnt.keys())
    noise = min(nonzero, key=lambda c: cnt[c])
    bg = max(nonzero, key=lambda c: cnt[c])
    shapes_cols = [c for c in nonzero if c != noise and c != bg]
    clusters = []
    for c in shapes_cols:
        pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == c]
        if not pts:
            continue
        rs = [i for i, _ in pts]
        cs = [j for _, j in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        shape = [row[c0:c1+1] for row in grid[r0:r1+1]]
        clusters.append((r0, c0, shape))
    clusters.sort(key=lambda x: (x[0], x[1]))
    shapes = [shape for _, _, shape in clusters]
    n = len(shapes)
    b = 2
    hs = [len(s) for s in shapes]
    ws = [len(s[0]) for s in shapes]
    wL = max(ws[0] if n>0 else 0, ws[3] if n>3 else 0)
    wR = max(ws[1] if n>1 else 0, ws[2] if n>2 else 0)
    hT = max(hs[0] if n>0 else 0, hs[1] if n>1 else 0)
    hB = max(hs[2] if n>2 else 0, hs[3] if n>3 else 0)
    H = hT + hB + 2*b
    W = wL + wR + 2*b
    out = [[bg] * W for _ in range(H)]
    pos = [(b, b), (b, b + wL), (b + hT, b + wL), (b + hT, b)]
    if n == 4:
        order = [3, 2, 0, 1]
    else:
        order = list(range(n))
    for i in range(min(n, 4)):
        si = order[i]
        sh = shapes[si]
        r0, c0 = pos[i]
        for di in range(len(sh)):
            for dj in range(len(sh[0])):
                out[r0+di][c0+dj] = sh[di][dj]
    return out