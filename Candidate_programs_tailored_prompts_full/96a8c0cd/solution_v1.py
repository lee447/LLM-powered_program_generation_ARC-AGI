def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    anchor = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                anchor = (r, c)
                break
        if anchor: break
    bars = []
    for r in range(h):
        for c in range(w):
            col = grid[r][c]
            if col in (1, 3):
                if c + 2 < w and grid[r][c+1] == col and grid[r][c+2] == col:
                    if c-1 < 0 or grid[r][c-1] != col:
                        bars.append(('h', r, c))
                if r + 2 < h and grid[r+1][c] == col and grid[r+2][c] == col:
                    if r-1 < 0 or grid[r-1][c] != col:
                        bars.append(('v', r, c))
    ar, ac = anchor
    for orient, r, c in bars:
        if orient == 'h':
            mr, mc = r, c+1
            d = 1 if ac > mc else -1
            cc = mc + d
            for dr in (-1, 0, 1):
                rr = mr + dr
                if 0 <= rr < h and 0 <= cc < w:
                    res[rr][cc] = 2
        else:
            mr, mc = r+1, c
            d = 1 if ar > mr else -1
            rr = mr + d
            for dc in (-1, 0, 1):
                cc = mc + dc
                if 0 <= rr < h and 0 <= cc < w:
                    res[rr][cc] = 2
    return res