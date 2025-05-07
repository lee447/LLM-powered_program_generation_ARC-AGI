def solve(grid):
    H = len(grid)
    W = len(grid[0])
    def find_period(length, get_cell):
        for p in range(1, length):
            ok = True
            for i in range(length - p):
                for j in range((W if get_cell == (lambda x,y: None) else H)):
                    a = get_cell(i, j)
                    b = get_cell(i + p, j)
                    if a != 0 and b != 0 and a != b:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return p
        return length
    p = find_period(H, lambda i, j: grid[i][j])
    q = find_period(W, lambda j, i: grid[i][j])
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