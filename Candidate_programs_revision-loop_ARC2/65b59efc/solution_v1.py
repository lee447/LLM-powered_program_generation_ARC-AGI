def solve(grid):
    R, C = len(grid), len(grid[0])
    sep_r = [i for i in range(R) if len(set(grid[i])) > 2]
    sep_c = [j for j in range(C) if len({grid[i][j] for i in range(R)}) > 2]
    rows = [0] + sep_r + [R]
    cols = [0] + sep_c + [C]
    blocks = []
    for bi in range(len(rows)-1):
        r0, r1 = rows[bi]+1, rows[bi+1]
        row_blocks = []
        for bj in range(len(cols)-1):
            c0, c1 = cols[bj]+1, cols[bj+1]
            block = [row[c0:c1] for row in grid[r0:r1]]
            row_blocks.append(block)
        blocks.append(row_blocks)
    def norm(b):
        h, w = len(b), len(b[0])
        m = max(max(row) for row in b)
        return tuple(tuple(1 if b[i][j]==m else 0 for j in range(w)) for i in range(h))
    pats = {}
    nextcol = 1
    T = []
    for i in range(len(blocks)):
        row = []
        for j in range(len(blocks[0])):
            p = norm(blocks[i][j])
            if p not in pats:
                pats[p] = nextcol
                nextcol += 1
            row.append(pats[p])
        T.append(row)
    bh = len(T[0][0] if T else 0) or len(blocks[0][0])
    bw = len(blocks[0][0][0]) if blocks and blocks[0] else 0
    H = len(T)*bh
    W = len(T[0])*bw
    out = [[0]*W for _ in range(H)]
    for i in range(len(T)):
        for j in range(len(T[0])):
            p = norm(blocks[i][j])
            col = pats[p]
            for di in range(bh):
                for dj in range(bw):
                    if p[di][dj]:
                        out[i*bh+di][j*bw+dj] = col
    return out