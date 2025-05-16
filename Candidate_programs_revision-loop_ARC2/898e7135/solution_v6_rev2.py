from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0:
                cnt[c] = cnt.get(c, 0) + 1
    nonzero = list(cnt.keys())
    noise = min(nonzero, key=lambda c: cnt[c])
    bg = max(nonzero, key=lambda c: cnt[c])
    shapes_cols = [c for c in nonzero if c != noise and c != bg]
    clusters = {}
    for c in shapes_cols:
        pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == c]
        rs = [i for i, _ in pts]
        cs = [j for _, j in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        shape = [row[c0:c1+1] for row in grid[r0:r1+1]]
        clusters[(r0, c0)] = shape
    items = sorted(clusters.items(), key=lambda x: (x[0][0], x[0][1]))
    shapes = [shape for _, shape in items]
    n = len(shapes)
    b = 2
    for i in (2, 3):
        if i < n:
            sh = shapes[i]
            Hs, Ws = len(sh), len(sh[0])
            rot = [[0] * Hs for _ in range(Ws)]
            for ii in range(Hs):
                for jj in range(Ws):
                    rot[jj][Hs-1-ii] = sh[ii][jj]
            shapes[i] = rot
    hs = [len(s) for s in shapes]
    ws = [len(s[0]) for s in shapes]
    hT = max(hs[0] if n>0 else 0, hs[1] if n>1 else 0)
    hB = max(hs[2] if n>2 else 0, hs[3] if n>3 else 0)
    wL = max(ws[0] if n>0 else 0, ws[2] if n>2 else 0)
    wR = max(ws[1] if n>1 else 0, ws[3] if n>3 else 0)
    H = hT + hB + 2*b
    W = wL + wR + 2*b
    out = [[bg] * W for _ in range(H)]
    pos = [(b, b), (b, b + wL), (b + hT, b + wL), (b + hT, b)]
    for i in range(min(n, 4)):
        sh = shapes[i]
        si, sj = len(sh), len(sh[0])
        r0, c0 = pos[i]
        if i % 2 == 1:
            c0 += ( (wR if i<3 else wL) - sj )
        for di in range(si):
            for dj in range(sj):
                out[r0+di][c0+dj] = sh[di][dj]
    return out