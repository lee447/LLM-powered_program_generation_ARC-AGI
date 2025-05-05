def solve(grid):
    H, W = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    out = [row[:] for row in grid]
    for r in range(H):
        for c in range(W):
            if orig[r][c] == 1:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < H and 0 <= nc < W and orig[nr][nc] == 0:
                            out[nr][nc] = 1
    return out