def solve(grid):
    n = len(grid)
    m = len(grid[0])
    r0 = n; r1 = -1; c0 = m; c1 = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    H = r1 - r0 + 1
    W = c1 - c0 + 1
    for dr, dc, rev_r, rev_c in [(-H, 0, False, False), (H, 0, True, False), (0, -W, False, True), (0, W, False, False)]:
        rr = r0 + dr
        cc = c0 + dc
        if 0 <= rr and rr + H <= n and 0 <= cc and cc + W <= m:
            ok = True
            for i in range(H):
                for j in range(W):
                    if grid[rr + i][cc + j] == 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                mat = [[grid[rr + i][cc + j] for j in range(W)] for i in range(H)]
                if rev_r:
                    mat = mat[::-1]
                if rev_c:
                    mat = [row[::-1] for row in mat]
                return mat
    return []