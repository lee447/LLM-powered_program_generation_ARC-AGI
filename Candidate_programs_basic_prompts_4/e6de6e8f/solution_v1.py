def solve(grid):
    h, w = len(grid), len(grid[0])
    cols = []
    for j in range(w):
        if grid[0][j] or grid[1][j]:
            cols.append((grid[0][j] > 0, grid[1][j] > 0))
    R, C = len(cols), 7
    out = [[0]*C for _ in range(R)]
    r, c = 0, 3
    out[0][c] = 3
    dir = 1
    for i in range(1, R):
        b0, b1 = cols[i]
        if b0 and b1:
            # horizontal
            c2 = c + dir
            x1, x2 = min(c, c2), max(c, c2)
            out[i][x1] = out[i][x2] = 2
            c = c2
        elif b0:
            # diagonal up‐right or down‐right
            c2 = c + 1
            out[i][c] = out[i][c2] = 2
            c = c2
            dir = 1
        elif b1:
            # diagonal up‐left or down‐left
            c2 = c - 1
            out[i][c] = out[i][c2] = 2
            c = c2
            dir = -1
        else:
            # vertical
            out[i][c] = 2
    return out