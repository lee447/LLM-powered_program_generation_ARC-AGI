def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    rows = [i for i in range(h) if all(grid[i][j] == border for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j] == border for i in range(h))]
    if rows[0] != 0: rows = [0] + rows
    if rows[-1] != h-1: rows.append(h-1)
    if cols[0] != 0: cols = [0] + cols
    if cols[-1] != w-1: cols.append(w-1)
    rows.sort(); cols.sort()
    rsegs = [(rows[i]+1, rows[i+1]-1) for i in range(len(rows)-1) if rows[i+1]-rows[i]>1]
    csegs = [(cols[j]+1, cols[j+1]-1) for j in range(len(cols)-1) if cols[j+1]-cols[j]>1]
    R, C = len(rsegs), len(csegs)
    avail = [[any(grid[r][c] != border for r in range(rsegs[i][0], rsegs[i][1]+1) for c in range(csegs[j][0], csegs[j][1]+1)) for j in range(C)] for i in range(R)]
    m = min(R, C)
    k = 1
    for s in range(2, m+1):
        ok = True
        for i in range(s):
            for j in range(s):
                if not avail[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            k = s
    if k >= 2:
        br0, br1 = 0, k-1
        bc0, bc1 = 0, k-1
    else:
        col_ok = next((j for j in range(C) if all(avail[i][j] for i in range(R))), None)
        if col_ok is not None:
            br0, br1 = 0, R-1
            bc0 = bc1 = col_ok
        else:
            row_ok = next((i for i in range(R) if all(avail[i][j] for j in range(C))), 0)
            br0 = br1 = row_ok
            bc0, bc1 = 0, C-1
    r0 = rows[br0]
    r1 = rows[br1+1]
    c0 = cols[bc0]
    c1 = cols[bc1+1]
    out = []
    for i in range(r0, r1+1):
        row = []
        for j in range(c0, c1+1):
            if grid[i][j] == border:
                row.append(border)
            else:
                bi = next(bi for bi,(a,b) in enumerate(rsegs) if a <= i <= b)
                bj = next(bj for bj,(a,b) in enumerate(csegs) if a <= j <= b)
                if k >= 2:
                    color = next(grid[a][b] for a in range(rsegs[bi][0], rsegs[bi][1]+1) for b in range(csegs[k-1][0], csegs[k-1][1]+1) if grid[a][b] != border)
                else:
                    if col_ok is not None:
                        color = next(grid[a][b] for a in range(rsegs[bi][0], rsegs[bi][1]+1) for b in range(csegs[col_ok][0], csegs[col_ok][1]+1) if grid[a][b] != border)
                    else:
                        color = next(grid[a][b] for a in range(rsegs[row_ok][0], rsegs[row_ok][1]+1) for b in range(csegs[bj][0], csegs[bj][1]+1) if grid[a][b] != border)
                row.append(color)
        out.append(row)
    return out