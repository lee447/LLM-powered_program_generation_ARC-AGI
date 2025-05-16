def solve(grid):
    H, W = len(grid), len(grid[0])
    # find horizontal segments by constant first-row runs
    col_segs = []
    x = grid[0][0]
    cnt = 0
    for c in range(W):
        if grid[0][c] == x:
            cnt += 1
        else:
            col_segs.append(cnt)
            x = grid[0][c]
            cnt = 1
    col_segs.append(cnt)
    # find vertical segments by constant first-column runs
    row_segs = []
    y = grid[0][0]
    cnt = 0
    for r in range(H):
        if grid[r][0] == y:
            cnt += 1
        else:
            row_segs.append(cnt)
            y = grid[r][0]
            cnt = 1
    row_segs.append(cnt)
    # compute starts
    col_starts = [0]
    for v in col_segs[:-1]:
        col_starts.append(col_starts[-1] + v)
    row_starts = [0]
    for v in row_segs[:-1]:
        row_starts.append(row_starts[-1] + v)
    # build macrogrid colors
    R = len(row_segs)
    C = len(col_segs)
    macro = [[grid[row_starts[r]][col_starts[c]] for r in range(R)] for c in range(C)]
    # dispatch into output bands: swap axes
    outH = sum(col_segs)
    outW = sum(row_segs)
    out = [[0]*outW for _ in range(outH)]
    # fill blocks
    # block dims: output rows by col_segs, output cols by row_segs
    for bi in range(C):
        for bj in range(R):
            color = macro[bi][bj]
            r0 = sum(col_segs[:bi])
            c0 = sum(row_segs[:bj])
            for dr in range(col_segs[bi]):
                for dc in range(row_segs[bj]):
                    out[r0+dr][c0+dc] = color
    return out