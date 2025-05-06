def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) if all(c == 0 for c in grid[i])]
    cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    rsegs = [(rows[i]+1, rows[i+1]) for i in range(len(rows)-1)]
    csegs = [(cols[j]+1, cols[j+1]) for j in range(len(cols)-1)]
    out = [row[:] for row in grid]
    for bi, (r0, r1) in enumerate(rsegs):
        for bj, (c0, c1) in enumerate(csegs):
            block = [grid[r][c0:c1] for r in range(r0, r1)]
            cnt = {}
            for row in block:
                for v in row:
                    if v:
                        cnt[v] = cnt.get(v,0) + 1
            if not cnt: continue
            fg = min(cnt, key=cnt.get)
            bg = max(cnt, key=cnt.get)
            B = r1 - r0
            A = c1 - c0
            # rotate fg points 90° cw about block-center
            pts = [(i,j) for i in range(B) for j in range(A) if block[i][j]==fg]
            new = [[bg]*A for _ in range(B)]
            for i,j in pts:
                di, dj = i - B//2, j - A//2
                ni, nj = dj, -di
                oi, oj = ni + B//2, nj + A//2
                if 0 <= oi < B and 0 <= oj < A:
                    new[oi][oj] = fg
            for i in range(B):
                for j in range(A):
                    out[r0+i][c0+j] = new[i][j]
    return out