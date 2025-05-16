def solve(grid):
    h, w = len(grid), len(grid[0])
    cols = [c for c in range(w) if all(grid[r][c] == grid[0][c] for r in range(h))]
    min_b, max_b = cols[0], cols[-1]
    left_bg = grid[0][min_b-1]
    right_bg = grid[0][max_b+1]
    shape = [(r, c, grid[r][c]) for r in range(h) for c in range(min_b)
             if grid[r][c] not in (left_bg, right_bg, grid[0][0], grid[0][-1], grid[0][min_b], grid[0][max_b])]
    if not shape:
        return grid
    min_r = min(r for r, _, _ in shape)
    max_r = max(r for r, _, _ in shape)
    mid_r = (0 + h - 1) // 2
    mid_s = (min_r + max_r) // 2
    dr = mid_r - mid_s
    mid_c = min_b + max_b
    out = [row[:] for row in grid]
    for r, c, _ in shape:
        out[r][c] = left_bg
    for r, c, v in shape:
        nr = r + dr
        nc = mid_c - c
        if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == right_bg:
            out[nr][nc] = v
    return out