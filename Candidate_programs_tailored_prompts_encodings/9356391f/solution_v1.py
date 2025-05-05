def solve(grid):
    H, W = len(grid), len(grid[0])
    palette = [v for v in grid[0] if v != 0]
    anchor_r = anchor_c = None
    for r in range(2, H):
        for c in range(W):
            if grid[r][c] != 0:
                anchor_r, anchor_c = r, c
                break
        if anchor_r is not None:
            break
    out = [row[:] for row in grid]
    for k in range(len(palette), 0, -1):
        r = k - 1
        color = palette[k - 1]
        for i in range(anchor_r - r, anchor_r + r + 1):
            if i <= 1 or i < 0 or i >= H:
                continue
            for j in range(anchor_c - r, anchor_c + r + 1):
                if 0 <= j < W:
                    out[i][j] = color
    return out