def solve(grid):
    h, w = len(grid), len(grid[0])
    color = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                color = grid[r][c]
                break
        if color is not None:
            break
    minr, maxr = h, -1
    minc, maxc = w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == color:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    out = [[0] * w for _ in range(h)]
    for r in range(minr, maxr + 1):
        i = r - minr
        m = i % 4
        if m == 1:
            off = -1
        elif m == 3:
            off = 1
        else:
            off = 0
        for c in range(minc, maxc + 1):
            if grid[r][c] == color:
                nc = c + off
                if 0 <= nc < w:
                    out[r][nc] = color
    return out