def solve(grid):
    H, W = len(grid), len(grid[0])
    bestP, bestPr = 1, -1.0
    for P in range(1, H):
        if H % P: continue
        tot = (H - P) * W
        if tot == 0: continue
        m = 0
        for r in range(H - P):
            row_r = grid[r]
            row_rp = grid[r + P]
            for c in range(W):
                if row_r[c] == row_rp[c]:
                    m += 1
        mr = m / tot
        if mr > bestPr:
            bestPr, bestP = mr, P
    bestQ, bestQr = 1, -1.0
    for Q in range(1, W):
        if W % Q: continue
        tot = H * (W - Q)
        if tot == 0: continue
        m = 0
        for r in range(H):
            row = grid[r]
            for c in range(W - Q):
                if row[c] == row[c + Q]:
                    m += 1
        mr = m / tot
        if mr > bestQr:
            bestQr, bestQ = mr, Q
    P, Q = bestP, bestQ
    out = []
    for u in range(P):
        row = []
        for v in range(Q):
            cnt = {}
            for r in range(u, H, P):
                for c in range(v, W, Q):
                    cnt[grid[r][c]] = cnt.get(grid[r][c], 0) + 1
            val = max(cnt.items(), key=lambda x: x[1])[0]
            row.append(val)
        out.append(row)
    return out