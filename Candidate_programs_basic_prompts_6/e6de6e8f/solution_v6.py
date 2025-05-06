def solve(grid):
    cols = [j for j in range(len(grid[0])) if grid[0][j] or grid[1][j]]
    n = len(cols)
    h, w = n, n - 1
    out = [[0]*w for _ in range(h)]
    center = w//2
    out[0][center] = 3
    for i, c in enumerate(cols[1:], 1):
        a, b = grid[0][c], grid[1][c]
        if a and b:
            out[i][center] = 2
            out[i][center+1] = 2
        else:
            out[i][center + (1 if b else 0)] = 2
    return out