def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) if all(grid[i][j]==0 for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    brs = []
    for bi in range(len(rows)-1):
        r0, r1 = rows[bi]+1, rows[bi+1]-1
        for bj in range(len(cols)-1):
            c0, c1 = cols[bj]+1, cols[bj+1]-1
            if r1-r0==4 and c1-c0==4:
                brs.append((r0, r1, c0, c1))
    out = [row[:] for row in grid]
    for idx, (r0, r1, c0, c1) in enumerate(brs):
        interior = [(i, j) for i in range(r0+1, r1) for j in range(c0+1, c1)]
        col = grid[r0][c0]
        cnt = sum(1 for i,j in interior if grid[i][j]!=0)
        has_h = any(all(grid[r0+1+k][c0+1+l]!=0 for l in range(3)) for k in range(3))
        has_v = any(all(grid[r0+1+k][c0+1+l]!=0 for k in range(3)) for l in range(3))
        if not has_h and not has_v:
            if cnt>0:
                has_h = cnt==3 and any(all(grid[r0+1+k][c0+1+l]!=0 for l in range(3)) for k in range(3))
                has_v = cnt==3 and any(all(grid[r0+1+k][c0+1+l]!=0 for k in range(3)) for l in range(3))
        if has_h and not has_v:
            for i,j in interior:
                if j==c0+2:
                    out[i][j] = col
        elif has_v and not has_h:
            for i,j in interior:
                if i==r0+2:
                    out[i][j] = col
        elif has_h and has_v:
            for i,j in interior:
                if i==r0+2 or j==c0+2:
                    out[i][j] = col
    return out