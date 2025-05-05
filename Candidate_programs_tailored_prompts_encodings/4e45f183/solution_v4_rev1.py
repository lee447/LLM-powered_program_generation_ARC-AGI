def solve(grid):
    h, w = len(grid), len(grid[0])
    black_rows = [i for i in range(h) if all(x==0 for x in grid[i])]
    black_cols = [j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    row_ranges = [(black_rows[i]+1, black_rows[i+1]) for i in range(len(black_rows)-1)]
    col_ranges = [(black_cols[j]+1, black_cols[j+1]) for j in range(len(black_cols)-1)]
    out = [row[:] for row in grid]
    H = row_ranges[0][1] - row_ranges[0][0]
    W = col_ranges[0][1] - col_ranges[0][0]
    m = H//2
    maskE = [[(j==m or (j>m and abs(i-m)<=j-m)) for j in range(W)] for i in range(H)]
    maskW = [[(j==m or (j<m and abs(i-m)<=m-j)) for j in range(W)] for i in range(H)]
    maskN = [[(i==m or (i<m and abs(j-m)<=m-i)) for j in range(W)] for i in range(H)]
    maskS = [[(i==m or (i>m and abs(j-m)<=i-m)) for j in range(W)] for i in range(H)]
    maskD = [[(abs(i-m)+abs(j-m)<=m) for j in range(W)] for i in range(H)]
    for bi,(r0,r1) in enumerate(row_ranges):
        for bj,(c0,c1) in enumerate(col_ranges):
            cnt = {}
            for i in range(r0,r1):
                for j in range(c0,c1):
                    v = grid[i][j]
                    if v!=0:
                        cnt[v] = cnt.get(v,0)+1
            if not cnt: continue
            sc = max(cnt, key=cnt.get)
            bc = min(cnt, key=cnt.get)
            block = [grid[i][c0:c1] for i in range(r0,r1)]
            best, best_mask = -1, None
            for mask in (maskE,maskS,maskW,maskN,maskD):
                s = 0
                for i in range(H):
                    for j in range(W):
                        want = mask[i][j]
                        have = (block[i][j]==sc)
                        if want==have: s+=1
                if s>best:
                    best, best_mask = s, mask
            for i in range(H):
                for j in range(W):
                    out[r0+i][c0+j] = sc if best_mask[i][j] else bc
    return out