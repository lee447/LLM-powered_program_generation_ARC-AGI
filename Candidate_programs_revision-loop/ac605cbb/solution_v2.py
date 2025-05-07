def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    for r, c, v in pts:
        if v == 1:
            for i in range(1, 3):
                if 0 <= c + i < w:
                    out[r][c + i] = 5
            if 0 <= r - 1 < h and 0 <= c + 2 < w:
                out[r - 1][c + 2] = 1
        elif v == 2:
            dest = 1
            for i in range(1, c - dest + 1):
                x = c - i
                if 0 <= x < w:
                    out[r][x] = 5
            out[r][dest] = 2
        elif v == 3:
            for i in range(1, 3):
                y = r + i
                if 0 <= y < h:
                    out[y][c] = 5
            if r + 3 < h:
                out[r + 3][c] = 3
        elif v == 6:
            dest = 0
            for i in range(1, r - dest + 1):
                y = r - i
                if 0 <= y < h:
                    out[y][c] = 5
            out[dest][c] = 6
    return out