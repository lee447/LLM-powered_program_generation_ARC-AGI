def solve(grid):
    h = len(grid)
    w = len(grid[0])
    zr = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    zc = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    rs = [zr[i] + 1 for i in range(len(zr) - 1)]
    re = [zr[i + 1] for i in range(len(zr) - 1)]
    cs = [zc[i] + 1 for i in range(len(zc) - 1)]
    ce = [zc[i + 1] for i in range(len(zc) - 1)]
    blocks = []
    for bi in range(len(rs)):
        for bj in range(len(cs)):
            cnt = 0
            for i in range(rs[bi], re[bi]):
                for j in range(cs[bj], ce[bj]):
                    if grid[i][j] == 2:
                        cnt += 1
            blocks.append((cnt, bi, bj))
    vals = sorted({b[0] for b in blocks}, reverse=True)
    mp = {}
    for cnt, bi, bj in blocks:
        if cnt == vals[0]:
            mp[(bi, bj)] = 3
        elif len(vals) > 1 and cnt == vals[1]:
            mp[(bi, bj)] = 8
        else:
            mp[(bi, bj)] = 2
    out = [row[:] for row in grid]
    for (cnt, bi, bj) in blocks:
        c = mp[(bi, bj)]
        for i in range(rs[bi], re[bi]):
            for j in range(cs[bj], ce[bj]):
                if grid[i][j] == 2:
                    out[i][j] = c
    return out