def solve(grid):
    m, n = len(grid), len(grid[0])
    def find_period(is_row):
        L = m if is_row else n
        M = n if is_row else m
        for p in range(1, L):
            ok = True
            for i in range(L - p):
                for j in range(M):
                    a = grid[i][j] if is_row else grid[j][i]
                    b = grid[i + p][j] if is_row else grid[j][i + p]
                    if a != 0 and b != 0 and a != b:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return p
        return L
    r = find_period(True)
    c = find_period(False)
    out = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                out[i][j] = grid[i][j]
            else:
                out[i][j] = grid[i % r][j % c]
    return out