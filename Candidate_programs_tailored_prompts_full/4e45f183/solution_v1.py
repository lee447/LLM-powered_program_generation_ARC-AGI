def solve(grid):
    H, W = len(grid), len(grid[0])
    zero_rows = [r for r in range(H) if all(v == 0 for v in grid[r])]
    zero_cols = [c for c in range(W) if all(grid[r][c] == 0 for r in range(H))]
    sep_rows = [-1] + zero_rows + [H]
    sep_cols = [-1] + zero_cols + [W]
    row_blocks = [(sep_rows[i]+1, sep_rows[i+1]-1) for i in range(len(sep_rows)-1) if sep_rows[i]+1 <= sep_rows[i+1]-1]
    col_blocks = [(sep_cols[i]+1, sep_cols[i+1]-1) for i in range(len(sep_cols)-1) if sep_cols[i]+1 <= sep_cols[i+1]-1]
    R, C = len(row_blocks), len(col_blocks)
    blocks = [[None]*C for _ in range(R)]
    for bi, (r0, r1) in enumerate(row_blocks):
        for bj, (c0, c1) in enumerate(col_blocks):
            cnt = {}
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    v = grid[r][c]
                    cnt[v] = cnt.get(v,0)+1
            if 0 in cnt: del cnt[0]
            items = sorted(cnt.items(), key=lambda x: x[1])
            ac, bg = items[0][0], items[-1][0]
            shape = [(r-c0, c-c0) for r in range(r0,r1+1) for c in range(c0,c1+1) if grid[r][c]==ac]
            blocks[bi][bj] = (r0, r1, c0, c1, bg, ac, shape)
    out = [row[:] for row in grid]
    for bi in range(R):
        for bj in range(C):
            r0, r1, c0, c1, _, _, shape = blocks[bi][bj]
            _, _, _, _, nbg, nac, _ = blocks[bi][(bj+1)%C]
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    out[r][c] = nbg
            for dr, dc in shape:
                out[r0+dr][c0+dc] = nac
    return out