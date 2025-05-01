def solve(grid):
    H, W = len(grid), len(grid[0])
    coords = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                coords.setdefault(v, []).append((r, c))
    res = [[0]*W for _ in range(H)]
    for v, pts in coords.items():
        if len({r for r,_ in pts})>1:
            cols = sorted({c for _,c in pts})
            pivot = cols[len(cols)//2]
            rows = sorted({r for r,_ in pts})
            for r in range(rows[0], rows[-1]+1):
                res[r][pivot] = v
        else:
            for r,c in pts:
                res[r][c] = v
    return res