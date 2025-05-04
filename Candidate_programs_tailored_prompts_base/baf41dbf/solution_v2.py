def solve(grid):
    h = len(grid)
    w = len(grid[0])
    orig_rs = []
    orig_cs = []
    pinks = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == 3:
                orig_rs.append(r)
                orig_cs.append(c)
            elif v == 6:
                pinks.append((r, c))
    top = min(orig_rs)
    bottom = max(orig_rs)
    left = min(orig_cs)
    right = max(orig_cs)
    new_top, new_bottom, new_left, new_right = top, bottom, left, right
    for r, c in pinks:
        if top <= r <= bottom:
            if c < left:
                new_left = c + 1
            elif c > right:
                new_right = c - 1
        if left <= c <= right:
            if r < top:
                new_top = r + 1
            elif r > bottom:
                new_bottom = r - 1
    out = [[0]*w for _ in range(h)]
    for c in range(new_left, new_right+1):
        out[new_top][c] = 3
        out[new_bottom][c] = 3
    for r in range(new_top, new_bottom+1):
        out[r][new_left] = 3
        out[r][new_right] = 3
    for r, c in pinks:
        out[r][c] = 6
    return out