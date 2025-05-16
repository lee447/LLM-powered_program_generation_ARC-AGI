def solve(grid):
    H, W = len(grid), len(grid[0])
    # detect horizontal splits by run-length of uniform rows
    row_runs = []
    i = 0
    while i < H:
        j = i
        while j < H and grid[j] == grid[i]:
            j += 1
        row_runs.append((i, j))
        i = j
    # detect vertical splits by run-length of uniform columns
    col_runs = []
    j = 0
    while j < W:
        k = j
        while k < W and all(grid[r][k] == grid[r][j] for r in range(H)):
            k += 1
        col_runs.append((j, k))
        j = k
    # build output shape by swapping runs
    out_h = sum(r2 - r1 for _, (r1, r2) in enumerate(col_runs))
    out_w = sum(c2 - c1 for _, (c1, c2) in enumerate(row_runs))
    out = [[0]*out_w for _ in range(out_h)]
    # for each block in input at block-row b_i and block-col b_j
    for bi, (r1, r2) in enumerate(row_runs):
        for bj, (c1, c2) in enumerate(col_runs):
            # collect non-bg colors
            block = [grid[r][c] for r in range(r1,r2) for c in range(c1,c2)]
            bg = max(set(block), key=block.count)
            non = [x for x in block if x!=bg]
            color = non[0] if len(set(non))==1 else 0
            # target block position in output: transpose block indices with vertical flip
            obi = len(col_runs)-1-bj
            obj = bi
            # target bounds
            tr1 = sum(c2-c1 for _, (c1,c2) in enumerate(col_runs) if _<obi)
            tr2 = tr1 + (c2-c1)
            tc1 = sum(r2-r1 for _, (r1,r2) in enumerate(row_runs) if _<obj)
            tc2 = tc1 + (r2-r1)
            for rr in range(tr1,tr2):
                for cc in range(tc1,tc2):
                    out[rr][cc] = color
    return out