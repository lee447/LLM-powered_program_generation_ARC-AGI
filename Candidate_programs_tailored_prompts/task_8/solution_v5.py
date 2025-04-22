def solve(grid):
    H, W = len(grid), len(grid[0])
    sep_rows = [r for r in range(H) if all(grid[r][c]==0 for c in range(W))]
    sep_cols = [c for c in range(W) if all(grid[r][c]==0 for r in range(H))]
    branges = [(sep_rows[i]+1, sep_rows[i+1]-1) for i in range(len(sep_rows)-1)]
    cranges = [(sep_cols[j]+1, sep_cols[j+1]-1) for j in range(len(sep_cols)-1)]
    orig = grid
    new = [row[:] for row in grid]
    for bi,(r0,r1) in enumerate(branges):
        for bj,(c0,c1) in enumerate(cranges):
            corners = [(r0,c0),(r0,c1),(r1,c0),(r1,c1)]
            Lc = orig[r0][c0]
            fillc = None
            s = set()
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    v = orig[r][c]
                    if v!=0 and v!=Lc:
                        s.add(v)
            if s:
                fillc = s.pop()
            else:
                fillc = Lc
            if (bi+bj)%2==0:
                L_out, F_out = fillc, Lc
            else:
                L_out, F_out = Lc, fillc
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    if (r,c) in corners:
                        new[r][c] = L_out
                    else:
                        new[r][c] = F_out
    return new