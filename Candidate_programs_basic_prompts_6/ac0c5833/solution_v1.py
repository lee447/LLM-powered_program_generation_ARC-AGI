def solve(grid):
    h = len(grid)
    w = len(grid[0])
    sep_cols = sorted([c for c in range(w) if sum(grid[r][c] == 4 for r in range(h)) >= 2])
    sep_rows = sorted([r for r in range(h) if sum(grid[r][c] == 4 for c in range(w)) >= 2])
    xs = [-1] + sep_cols + [w]
    ys = [-1] + sep_rows + [h]
    # find base cell for the red shape
    red = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    br = min(r for r, c in red)
    bc = min(c for r, c in red)
    # find which cell it belongs to
    for yi in range(len(ys) - 1):
        if ys[yi] < br < ys[yi + 1]:
            by = yi
            top0 = ys[yi] + 1
            break
    for xi in range(len(xs) - 1):
        if xs[xi] < bc < xs[xi + 1]:
            bx = xi
            left0 = xs[xi] + 1
            break
    offs = [(r - top0, c - left0) for (r, c) in red]
    out = [row[:] for row in grid]
    for yi in range(len(ys) - 1):
        top = ys[yi] + 1
        bottom = ys[yi + 1]
        for xi in range(len(xs) - 1):
            left = xs[xi] + 1
            right = xs[xi + 1]
            cell_h = bottom - top
            cell_w = right - left
            # try to place
            for dr, dc in offs:
                r = top + dr
                c = left + dc
                if 0 <= r < h and 0 <= c < w and out[r][c] == 0:
                    out[r][c] = 2
    return out