def solve(grid):
    H, W = len(grid), len(grid[0])
    def find_row_period():
        for p in range(1, H):
            ok = True
            for i in range(H - p):
                for j in range(W):
                    a, b = grid[i][j], grid[i+p][j]
                    if a != 0 and b != 0 and a != b:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return p
        return H
    def find_col_period():
        for q in range(1, W):
            ok = True
            for j in range(W - q):
                for i in range(H):
                    a, b = grid[i][j], grid[i][j+q]
                    if a != 0 and b != 0 and a != b:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return q
        return W
    p = find_row_period()
    q = find_col_period()
    tile = [[0]*q for _ in range(p)]
    for i in range(p):
        for j in range(q):
            for r in range(i, H, p):
                for c in range(j, W, q):
                    v = grid[r][c]
                    if v != 0:
                        tile[i][j] = v
                        break
                if tile[i][j] != 0:
                    break
    return tile