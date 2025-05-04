def solve(grid):
    H, W = len(grid), len(grid[0])
    cols = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                cols.setdefault(v, []).append((r, c))
    shapes = []
    for v, pts in cols.items():
        xs = [c for r,c in pts]
        ys = [r for r,c in pts]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        shape = {(r - ymin, c - xmin) for r, c in pts}
        shapes.append((sum(xs)/len(xs), v, ymin, xmin, ymax, xmax, shape))
    shapes.sort(key=lambda x: x[0])
    out = [[0]*W for _ in range(H)]
    for side, st in enumerate(shapes):
        _, v, ymin, xmin, ymax, xmax, shape = st
        h, w = ymax - ymin + 1, xmax - xmin + 1
        # rotate CW: (y,x)->(x, h-1-y)
        rot = {(x, h-1-y) for y,x in shape}
        rh = max(r for r,c in rot) + 1
        rw = max(c for r,c in rot) + 1
        if side == 0:
            roffs = H - rh
            coffs = 0
        else:
            roffs = H - rh
            coffs = W - rw
        for r, c in rot:
            out[roffs + r][coffs + c] = v
    return out