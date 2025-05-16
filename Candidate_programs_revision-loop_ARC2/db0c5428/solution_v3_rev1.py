def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bg = grid[0][0]
    min_r, max_r, min_c, max_c = h, -1, w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != bg:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    if max_r < 0:
        return grid
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    def divisors(n):
        d = []
        for x in range(1, n+1):
            if n % x == 0:
                d.append(x)
        return d
    possible_bs_r = [bs for bs in divisors(H) if H // bs > 1 and (H // bs) % 2 == 1]
    possible_bs_c = [bs for bs in divisors(W) if W // bs > 1 and (W // bs) % 2 == 1]
    bs_r = possible_bs_r[0]
    bs_c = possible_bs_c[0]
    block_count_r = H // bs_r
    block_count_c = W // bs_c
    m_r = block_count_r // 2
    m_c = block_count_c // 2
    blocks = []
    for i in range(block_count_r):
        row_blocks = []
        for j in range(block_count_c):
            blk = []
            for bi in range(bs_r):
                r0 = min_r + i * bs_r + bi
                blk.append(grid[r0][min_c + j * bs_c : min_c + (j + 1) * bs_c])
            row_blocks.append(blk)
        blocks.append(row_blocks)
    out = [row[:] for row in grid]
    for i in range(block_count_r):
        for j in range(block_count_c):
            if i == m_r and j == m_c:
                continue
            blk = blocks[i][j]
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    newblk = blk
                    if dr != 0:
                        newblk = newblk[::-1]
                    if dc != 0:
                        newblk = [row[::-1] for row in newblk]
                    r0 = min_r + (i + dr) * bs_r
                    c0 = min_c + (j + dc) * bs_c
                    for bi in range(bs_r):
                        rr = r0 + bi
                        if rr < 0 or rr >= h:
                            continue
                        for bj in range(bs_c):
                            cc = c0 + bj
                            if cc < 0 or cc >= w:
                                continue
                            if grid[rr][cc] == bg:
                                out[rr][cc] = newblk[bi][bj]
    return out