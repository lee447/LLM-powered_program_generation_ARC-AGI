import copy
def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    threshold = 2 if H <= 10 else 3
    for c in range(W):
        rows = [r for r in range(H) if grid[r][c] != 0]
        vals = {grid[r][c] for r in rows}
        if len(vals) >= threshold:
            first = rows[0]
            v0 = grid[first][c]
            for r in range(first):
                out[r][c] = v0
            for i in range(len(rows)-1):
                a = rows[i]
                b = rows[i+1]
                v = grid[b][c]
                for r in range(a+1, b):
                    out[r][c] = v
    return out