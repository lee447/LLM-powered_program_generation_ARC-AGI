def solve(grid):
    h, w = len(grid), len(grid[0])
    top = 0
    while top < h and any(grid[top][j] != grid[top][0] for j in range(w)):
        top += 1
    top += 1
    bg = grid[top][0]
    sh = top - 1
    out_h = h - sh
    out = [[bg] * w for _ in range(out_h)]
    blocks = []
    i = 1
    while i < top:
        j = 0
        while j < w:
            if grid[i][j] != grid[0][0] and grid[i][j] != 0:
                c = grid[i][j]
                ii, jj = i, j
                while ii < top and any(grid[ii][k] != grid[0][0] for k in range(j, j+1)):
                    ii += 1
                while jj < w and any(grid[k][jj] != grid[0][0] for k in range(i, ii)):
                    jj += 1
                blocks.append((i, j, ii-i, jj-j))
                j = jj
            else:
                j += 1
        i += 1
    for idx, (r, c, H, W) in enumerate(blocks):
        shape = [(dr, dc) for dr in range(H) for dc in range(W) if grid[r+dr][c+dc] != 0 and grid[r+dr][c+dc] != grid[0][0]]
        if idx == 0:
            for dr, dc in shape:
                for k in range(W):
                    rr = dr
                    cc = c - blocks[0][1] + sh - 1 + k
                    out[rr][cc] = 8
        if idx == 1:
            for dr, dc in shape:
                for k in range(H):
                    rr = dr - blocks[1][0] + k
                    cc = c + dc * 0 + (c - blocks[1][1]) + W - 1 + 1
                    out[rr][cc] = 8
        if idx == 2:
            for dr, dc in shape:
                for k in range(W):
                    rr = out_h - sh + blocks[2][0] - r + k - 1
                    cc = c - blocks[2][1] + sh + dr
                    if 0 <= rr < out_h:
                        out[rr][cc] = 8
        if idx == 3:
            for dr, dc in shape:
                for k in range(H):
                    rr = out_h - sh + blocks[3][0] - r + dr
                    cc = dc + c - blocks[3][1] - k
                    if 0 <= rr < out_h and 0 <= cc < w:
                        out[rr][cc] = 8
    for i in range(sh, out_h):
        for j in range(w):
            out[i][j] = grid[i+sh][j]
    return out