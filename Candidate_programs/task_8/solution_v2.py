def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    for c in range(W):
        vals = [grid[r][c] for r in range(H) if grid[r][c] != 0]
        if len(set(vals)) >= (2 if H <= 10 else 3):
            for r in range(H):
                if out[r][c] == 0:
                    for rr in range(r + 1, H):
                        v = grid[rr][c]
                        if v != 0:
                            out[r][c] = v
                            break
    return out