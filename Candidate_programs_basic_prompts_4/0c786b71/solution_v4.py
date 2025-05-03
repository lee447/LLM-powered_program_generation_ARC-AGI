def solve(grid):
    H, W = len(grid), len(grid[0])
    R = [row[::-1] for row in grid[::-1]]
    out = [[0] * (2 * W) for _ in range(2 * H)]
    for i in range(2 * H):
        ri = i if i < H else 2 * H - 1 - i
        for j in range(2 * W):
            cj = j if j < W else 2 * W - 1 - j
            out[i][j] = R[ri][cj]
    return out