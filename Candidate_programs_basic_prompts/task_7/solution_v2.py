def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_r = [i for i,row in enumerate(grid) if all(c==4 for c in row)]
    sep_c = [j for j in range(w) if all(grid[i][j]==4 for i in range(h))]
    rs = [-1]+sep_r+[h]
    cs = [-1]+sep_c+[w]
    out = [row[:] for row in grid]
    for bi in range(len(rs)-1):
        r0, r1 = rs[bi]+1, rs[bi+1]-1
        if r0>r1: continue
        for bj in range(len(cs)-1):
            c0, c1 = cs[bj]+1, cs[bj+1]-1
            if c0>c1: continue
            block = [out[r][c0:c1+1] for r in range(r0,r1+1)]
            m = {}
            for i in range(len(block)):
                for j in range(len(block[0])):
                    v = block[i][j]
                    if v not in (0,4,1): m[v]=True
            if not m: continue
            col = next(iter(m))
            for i in range(len(block)):
                for j in range(len(block[0])):
                    if block[i][j]==col and block[j][i]==0:
                        out[r0+j][c0+i]=col
    return out