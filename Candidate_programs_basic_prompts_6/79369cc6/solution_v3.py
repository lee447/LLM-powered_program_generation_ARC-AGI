def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    rmin = min(r for r, c in pts)
    rmax = max(r for r, c in pts)
    cmin = min(c for r, c in pts)
    cmax = max(c for r, c in pts)
    mask = [[1 if grid[rmin + i][cmin + j] == 4 else 0 for j in range(cmax - cmin + 1)] for i in range(rmax - rmin + 1)]
    shifts = [(-rmin + 1, W - 1 - cmax), (H - 1 - rmax, -cmin + 1)]
    out = [row[:] for row in grid]
    for dr, dc in shifts:
        for i in range(len(mask)):
            for j in range(len(mask[0])):
                if mask[i][j]:
                    r, c = i + rmin + dr, j + cmin + dc
                    if 0 <= r < H and 0 <= c < W:
                        out[r][c] = 4
    return out