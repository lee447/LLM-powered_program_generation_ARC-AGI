def solve(grid):
    h = len(grid)
    w = len(grid[0])
    color = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                color = grid[r][c]
                break
        if color:
            break
    min_r, max_r = h, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == color:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == color:
                d = (r - min_r) % 4
                if d == 1:
                    dc = -1
                elif d == 3:
                    dc = 1
                else:
                    dc = 0
                out[r][c+dc] = color
    return out