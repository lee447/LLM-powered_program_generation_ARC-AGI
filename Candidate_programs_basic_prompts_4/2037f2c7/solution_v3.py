def solve(grid):
    h, w = len(grid), len(grid[0])
    best = (0, 0, 0)
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0:
                continue
            k = 1
            while True:
                if r-k < 0 or r+k >= h or c-k < 0 or c+k >= w:
                    break
                ok = True
                for j in range(c-k, c+k+1):
                    if grid[r-k][j] == 0 or grid[r+k][j] == 0:
                        ok = False
                        break
                if not ok:
                    break
                for i in range(r-k, r+k+1):
                    if grid[i][c-k] == 0 or grid[i][c+k] == 0:
                        ok = False
                        break
                if not ok:
                    break
                k += 1
            if k-1 > best[0]:
                best = (k-1, r, c)
    K, cr, cc = best
    k = K
    top, left = cr-k, cc-k
    sl = [grid[i][left:left+2*k+1] for i in range(top, top+2*k+1)]
    ringc = sl[0][0]
    n = 2*k+1
    mask = [[8 if sl[i][j] == ringc else 0 for j in range(n)] for i in range(n)]
    h_out = n - 4
    off = (n - h_out)//2
    return mask[off:off+h_out]