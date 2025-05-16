def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bg = grid[0][0]
    min_r, max_r, min_c, max_c = h, -1, w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != bg:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    if max_r < 0:
        return grid
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    cand = []
    for d in range(2, min(6, H) + 1):
        if H % d == 0 and W % d == 0:
            cand.append(d)
    block_count = max(cand) if cand else 1
    bs_r = H // block_count
    bs_c = W // block_count
    blocks = []
    for i in range(block_count):
        row_blocks = []
        for j in range(block_count):
            blk = []
            for bi in range(bs_r):
                r0 = min_r + i * bs_r + bi
                blk.append(grid[r0][min_c + j * bs_c : min_c + (j + 1) * bs_c])
            row_blocks.append(blk)
        blocks.append(row_blocks)
    out = [row[:] for row in grid]
    for i in range(block_count):
        for j in range(block_count):
            blk = blocks[i][j]
            rb = [row[::-1] for row in blk[::-1]]
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0: continue
                    dest_i = i + dr
                    dest_j = j + dc
                    r0 = min_r + dest_i * bs_r
                    c0 = min_c + dest_j * bs_c
                    for bi in range(bs_r):
                        rr = r0 + bi
                        if rr < 0 or rr >= h: continue
                        for bj in range(bs_c):
                            cc = c0 + bj
                            if cc < 0 or cc >= w: continue
                            if grid[rr][cc] == bg:
                                out[rr][cc] = rb[bi][bj]
    return out