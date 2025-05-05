def solve(grid):
    H = len(grid)
    W = len(grid[0])
    cols = []
    for c in range(W):
        for r in range(H):
            if grid[r][c] not in (0,8):
                cols.append(c)
                break
    cols = sorted(cols)
    c1 = grid[0][cols[0]]
    c2 = grid[0][cols[1]]
    c3 = grid[0][cols[2]]
    out = [[0 if v==8 else v for v in row] for row in grid]
    for r in range(H):
        row = grid[r]
        segs = []
        c = 0
        while c < W:
            if row[c] == 8:
                s = c
                while c < W and row[c] == 8:
                    c += 1
                segs.append((s, c-1))
            else:
                c += 1
        for i,(s,e) in enumerate(segs):
            order = [c1, c2, c3] if i==0 else [c3, c2, c1]
            widths = [4,2,4]
            idx = s
            for color, w in zip(order, widths):
                for _ in range(w):
                    if idx > e:
                        break
                    out[r][idx] = color
                    idx += 1
                if idx > e:
                    break
    return out