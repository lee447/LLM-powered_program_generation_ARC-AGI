def solve(grid):
    n = len(grid)
    m = len(grid[0])
    orig = grid
    def find_h():
        for p in range(1, m):
            ok = True
            for i in range(n):
                for j in range(m - p):
                    a = orig[i][j]
                    b = orig[i][j + p]
                    if a != 0 and b != 0 and a != b:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return p
        return m
    def find_v():
        for q in range(1, n):
            ok = True
            for i in range(n - q):
                for j in range(m):
                    a = orig[i][j]
                    b = orig[i + q][j]
                    if a != 0 and b != 0 and a != b:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return q
        return n
    p = find_h()
    q = find_v()
    res = [row[:] for row in orig]
    for i in range(n):
        for j in range(m):
            if res[i][j] == 0:
                res[i][j] = orig[i % q][j % p]
    return res