def solve(grid):
    h, w = len(grid), len(grid[0])
    blocks = []
    for r in range(h-3):
        for c in range(w-3):
            col = grid[r][c]
            if col == 0: continue
            ok = True
            for i in range(4):
                for j in range(4):
                    v = grid[r+i][c+j]
                    if 1 <= i <= 2 and 1 <= j <= 2:
                        if v != 0: ok = False
                    else:
                        if v != col: ok = False
            if ok:
                blocks.append((r, c))
    hollows = []
    for r, c in blocks:
        col = grid[r][c]
        interior_zero = True
        for i in (1,2):
            for j in (1,2):
                if grid[r+i][c+j] != 0: interior_zero = False
        if interior_zero:
            hollows.append((r, c))
    hollows = sorted(hollows, key=lambda x: x[1])
    xs = [(c, c+3) for _, c in hollows]
    overlap = any(xs[i][0] <= xs[j][1] and xs[j][0] <= xs[i][1] for i in range(len(xs)) for j in range(i+1, len(xs)))
    if overlap and len(hollows) > 1:
        hollows = sorted(hollows, key=lambda x: x[0])
        out = [[0]*4 for _ in range(4*len(hollows))]
        for k, (r, c) in enumerate(hollows):
            for i in range(4):
                for j in range(4):
                    out[k*4+i][j] = grid[r+i][c+j]
    else:
        out = [[0]*(4*len(hollows)) for _ in range(4)]
        for k, (r, c) in enumerate(hollows):
            for i in range(4):
                for j in range(4):
                    out[i][k*4+j] = grid[r+i][c+j]
    return out