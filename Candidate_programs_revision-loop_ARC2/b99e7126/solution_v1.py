def solve(grid):
    h, w = len(grid), len(grid[0])
    # find border interval and block size
    rows = [i for i in range(h) if all(grid[i][j]==grid[i][0] for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j]==grid[0][j] for i in range(h))]
    br = rows[1]-rows[0]
    bc = cols[1]-cols[0]
    # extract blocks
    def block(r,c):
        return [row[c:c+bc] for row in grid[r:r+br]]
    blocks = {}
    for bi,r in enumerate(range(br// br, h, br+1)):
        pass
    # Actually dynamic partition:
    br = rows[1]-rows[0]
    bc = cols[1]-cols[0]
    row_bs = [(rows[i]+1, rows[i+1]-rows[i]-1) for i in range(len(rows)-1)]
    col_bs = [(cols[i]+1, cols[i+1]-cols[i]-1) for i in range(len(cols)-1)]
    # default block pattern from first block
    r0,c0 = row_bs[0][0], col_bs[0][0]
    default = tuple(tuple(grid[r0+i][c0+j] for j in range(col_bs[0][1])) for i in range(row_bs[0][1]))
    # find special in input
    spec = {}
    for bi,(r0,br_) in enumerate(row_bs):
        for bj,(c0,bc_) in enumerate(col_bs):
            b = tuple(tuple(grid[r0+i][c0+j] for j in range(bc_)) for i in range(br_))
            if b!=default:
                spec.setdefault(bi, []).append((bj,b))
    if not spec:
        return [row[:] for row in grid]
    R, blist = next(iter(spec.items()))
    cols_spec = [bj for bj,_ in blist]
    cols_spec.sort()
    C0, Ck = cols_spec[0], cols_spec[-1]
    # build output
    out = [row[:] for row in grid]
    for i in range(R+1):
        if i==R:
            cjs = [C0]
        else:
            cjs = [C0, Ck]
        for bj in cjs:
            b = dict(blist)[bj]
            r0,br_ = row_bs[i]
            c0,bc_ = col_bs[bj]
            for ii in range(br_):
                for jj in range(bc_):
                    out[r0+ii][c0+jj] = b[ii][jj]
    return out