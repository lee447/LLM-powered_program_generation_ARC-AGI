def solve(grid):
    H, W = len(grid), len(grid[0])
    bounds = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                if v not in bounds:
                    bounds[v] = [r, r, c, c]
                else:
                    b = bounds[v]
                    if r < b[0]: b[0] = r
                    if r > b[1]: b[1] = r
                    if c < b[2]: b[2] = c
                    if c > b[3]: b[3] = c
    rects = []
    for v, (r0, r1, c0, c1) in bounds.items():
        area = (r1 - r0 + 1) * (c1 - c0 + 1)
        rects.append((area, v, r0, r1, c0, c1))
    rects.sort(reverse=True)
    out = [[0]*W for _ in range(H)]
    for _, v, r0, r1, c0, c1 in rects:
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                out[r][c] = v
    return out