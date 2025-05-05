def solve(grid):
    H, W = len(grid), len(grid[0])
    result = [[0]*W for _ in range(H)]
    pts = {(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0}
    if not pts:
        return result
    color = next(grid[r][c] for r, c in pts if grid[r][c] != 0)
    h_rows = sorted({r for r, c in pts if c+1 < W and grid[r][c] == grid[r][c+1]})
    inner = h_rows[1:-1]
    if inner:
        target = inner[len(inner)//2]
    else:
        target = None
    v_cols = sorted({c for r, c in pts if r+1 < H and grid[r][c] == grid[r+1][c]})
    n_inner = len(inner)
    if n_inner == 0:
        seq = [-1, 0, 1, 0]
    elif n_inner == 1:
        seq = [-1, 0]
    else:
        seq = [1, 0, -1, 0]
    for y in h_rows:
        dx = 1 if y == target else 0
        for c in range(W):
            if (y, c) in pts:
                nc = c + dx
                if 0 <= nc < W:
                    result[y][nc] = color
    for i in range(len(h_rows) - 1):
        top = h_rows[i]
        bottom = h_rows[i+1]
        for r in range(top+1, bottom):
            j0 = r - top - 1
            dx = seq[(j0 + i) % len(seq)]
            for c in v_cols:
                if (r, c) in pts:
                    nc = c + dx
                    if 0 <= nc < W:
                        result[r][nc] = color
    return result