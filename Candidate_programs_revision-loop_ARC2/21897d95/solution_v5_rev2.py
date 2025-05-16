from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    # compute row‐block boundaries by high row‐to‐row change
    rows = [0]
    diffs = [sum(grid[r][c] != grid[r+1][c] for c in range(W)) for r in range(H-1)]
    for r, d in enumerate(diffs):
        if d * 2 > W:
            rows.append(r+1)
    rows.append(H)
    row_runs = [(rows[i], rows[i+1]) for i in range(len(rows)-1)]
    # compute col‐block boundaries by high col‐to‐col change
    cols = [0]
    diffs = [sum(grid[r][c] != grid[r][c+1] for r in range(H)) for c in range(W-1)]
    for c, d in enumerate(diffs):
        if d * 2 > H:
            cols.append(c+1)
    cols.append(W)
    col_runs = [(cols[i], cols[i+1]) for i in range(len(cols)-1)]
    # build output by transposing the block grid
    R = len(row_runs)
    C = len(col_runs)
    out = [[0]*R for _ in range(C)]
    # majority color of each input block
    maj = [[0]*C for _ in range(R)]
    for i, (r1, r2) in enumerate(row_runs):
        for j, (c1, c2) in enumerate(col_runs):
            cnt = {}
            for r in range(r1, r2):
                for c in range(c1, c2):
                    x = grid[r][c]
                    cnt[x] = cnt.get(x,0) + 1
            maj[i][j] = max(cnt, key=cnt.get)
    # output blocks in swapped order
    out_rows = [r2 - r1 for r1, r2 in col_runs]
    out_cols = [c2 - c1 for c1, c2 in row_runs]
    H2, W2 = sum(out_rows), sum(out_cols)
    res = [[0]*W2 for _ in range(H2)]
    r0 = 0
    for i, h in enumerate(out_rows):
        c0 = 0
        for j, w in enumerate(out_cols):
            color = maj[j][i]
            for dr in range(h):
                for dc in range(w):
                    res[r0+dr][c0+dc] = color
            c0 += w
        r0 += h
    return res