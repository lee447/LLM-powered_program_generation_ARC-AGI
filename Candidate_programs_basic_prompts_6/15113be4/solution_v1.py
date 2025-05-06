def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = next(c for row in grid for c in row if row.count(c) == h or [r[c] for r in grid].count(c) == w)
    hs = [i for i in range(h) if all(grid[i][j] == bg for j in range(w))]
    vs = [j for j in range(w) if all(grid[i][j] == bg for i in range(h))]
    rs = [0] + hs + [h]
    cs = [0] + vs + [w]
    out = [row[:] for row in grid]
    for bi in range(len(rs)-1):
        for bj in range(len(cs)-1):
            if bi>0 and bj>0 and rs[bi]-rs[bi-1]==3 and cs[bj]-cs[bj-1]==3:
                r0, c0 = rs[bi], cs[bj]
                topA = [(r0+i, c0+j) for i in range(3) for j in range(3) if grid[r0+i][c0+j]==1]
                for di,dj in topA:
                    for (ri,ci) in [(di,ci) for ci in range(c0, c0+3)] + [(r0+i, c0+j) for i in range(3) for j in range(3)]:
                        dr, dc = ri, ci
                        if out[dr][dc] in (0,1):
                            out[dr][dc] = next(c for c in range(10) if c not in {bg,4,8,6,3})
    return out