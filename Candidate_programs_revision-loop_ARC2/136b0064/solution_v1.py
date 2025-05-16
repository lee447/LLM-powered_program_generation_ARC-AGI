def solve(grid):
    h, w = len(grid), len(grid[0])
    cuts = [j for j in range(w) if any(grid[i][j]==4 for i in range(h))]
    cutc = cuts[0]
    rows = [i for i in range(h) if any(grid[i][j]==4 for j in range(w))]
    out = [[0]*cutc for _ in range(h)]
    blocks = []
    r0 = 0
    for r in rows+[h]:
        blocks.append((r0, r))
        r0 = r+1
    for bi,(rs,re) in enumerate(blocks):
        sub = [row[:cutc] for row in grid[rs:re]]
        cols = {}
        for i in range(len(sub)):
            for j in range(cutc):
                v = sub[i][j]
                if v and v!=grid[0][cuts[0]]: cols.setdefault(v, []).append((i,j))
        tag = None
        for i in range(rs,re):
            for j in range(cutc,w):
                v=grid[i][j]
                if v and v!=4:
                    tag=v
        for c,pts in cols.items():
            if tag is None or c!=tag:
                tag=c
                break
        pts = cols[tag]
        if not pts: continue
        ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
        bh, bw = max(ys)-min(ys)+1, max(xs)-min(xs)+1
        for (i,j) in pts:
            oi = rs + (i-min(ys))
            oj = j-min(xs)
            out[oi][oj] = tag
    return out