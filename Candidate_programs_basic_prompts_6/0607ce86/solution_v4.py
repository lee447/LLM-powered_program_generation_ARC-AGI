def solve(grid):
    H = len(grid)
    W = len(grid[0])
    row_density = [sum(1 for v in row if v != 0) for row in grid]
    max_rd = max(row_density)
    thr_rd = max_rd * 0.5
    row_flag = [d >= thr_rd for d in row_density]
    row_blocks = []
    i = 0
    while i < H:
        if row_flag[i]:
            j = i
            while j < H and row_flag[j]:
                j += 1
            row_blocks.append((i, j - i))
            i = j
        else:
            i += 1
    block_height = max(l for _, l in row_blocks) if row_blocks else H
    starts_y = [s for s, l in row_blocks if l == block_height]
    startY = starts_y[0] if starts_y else 0
    row_starts = [s for s, _ in row_blocks]
    if len(row_starts) > 1:
        dy = min(row_starts[i+1] - row_starts[i] for i in range(len(row_starts)-1))
    else:
        dy = block_height
    col_density = []
    for x in range(W):
        cnt = 0
        for y in range(startY, startY + block_height):
            if y < H and grid[y][x] != 0:
                cnt += 1
        col_density.append(cnt)
    max_cd = max(col_density)
    thr_cd = max_cd * 0.5
    col_flag = [d >= thr_cd for d in col_density]
    col_blocks = []
    j = 0
    while j < W:
        if col_flag[j]:
            k = j
            while k < W and col_flag[k]:
                k += 1
            col_blocks.append((j, k - j))
            j = k
        else:
            j += 1
    block_width = max(l for _, l in col_blocks) if col_blocks else W
    starts_x = [s for s, l in col_blocks if l == block_width]
    startX = starts_x[0] if starts_x else 0
    col_starts = [s for s, _ in col_blocks]
    if len(col_starts) > 1:
        dx = min(col_starts[i+1] - col_starts[i] for i in range(len(col_starts)-1))
    else:
        dx = block_width
    template = [row[startX:startX+block_width] for row in grid[startY:startY+block_height]]
    out = [[0]*W for _ in range(H)]
    y = startY
    while y < H:
        x = startX
        while x < W:
            for i in range(block_height):
                for j in range(block_width):
                    yy = y + i
                    xx = x + j
                    if 0 <= yy < H and 0 <= xx < W:
                        out[yy][xx] = template[i][j]
            x += dx
        y += dy
    return out