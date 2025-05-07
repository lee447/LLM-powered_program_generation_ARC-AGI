def solve(grid):
    h = len(grid)
    w = len(grid[0])
    best_zero = 10
    bi = bj = 0
    for i in range(h - 2):
        for j in range(w - 2):
            zc = 0
            for a in range(3):
                for b in range(3):
                    if grid[i + a][j + b] == 0:
                        zc += 1
            if zc < best_zero:
                best_zero = zc
                bi, bj = i, j
    T = [[grid[bi + a][bj + b] for b in range(3)] for a in range(3)]
    out = [row[:] for row in grid]
    for i in range(h - 2):
        for j in range(w - 2):
            match = False
            ok = True
            for a in range(3):
                for b in range(3):
                    v = grid[i + a][j + b]
                    if v != 0:
                        match = True
                        if v != T[a][b]:
                            ok = False
                            break
                if not ok:
                    break
            if ok and match:
                for a in range(3):
                    for b in range(3):
                        out[i + a][j + b] = T[a][b]
    return out