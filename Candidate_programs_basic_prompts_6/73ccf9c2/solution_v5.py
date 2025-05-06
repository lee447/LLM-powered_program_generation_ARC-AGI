def solve(grid):
    m, n = len(grid), len(grid[0])
    colors = {grid[i][j] for i in range(m) for j in range(n) if grid[i][j] != 0}
    if not colors:
        return []
    c = colors.pop()
    mask = [[grid[i][j] == c for j in range(n)] for i in range(m)]
    def rotate(mat):
        h, w = len(mat), len(mat[0])
        return [[mat[r][c] for r in range(h-1, -1, -1)] for c in range(w)]
    def match(sub):
        h2, w2 = len(sub), len(sub[0])
        for x in range(m - h2 + 1):
            for y in range(n - w2 + 1):
                ok = True
                for i in range(h2):
                    for j in range(w2):
                        if sub[i][j]:
                            if grid[x+i][y+j] != c:
                                ok = False
                                break
                        else:
                            if grid[x+i][y+j] == c:
                                ok = False
                                break
                    if not ok:
                        break
                if ok:
                    return True
        return False
    for h in range(1, m+1):
        for w in range(1, n+1):
            for i0 in range(m - h + 1):
                for j0 in range(n - w + 1):
                    P = [row[j0:j0+w] for row in mask[i0:i0+h]]
                    if not any(any(r) for r in P):
                        continue
                    # require several true cells
                    cnt = sum(r.count(True) for r in P)
                    if cnt < 2:
                        continue
                    found_all = True
                    Q = P
                    for _ in range(4):
                        if not match(Q):
                            found_all = False
                            break
                        Q = rotate(Q)
                    if found_all:
                        out = [[c if P[i][j] else 0 for j in range(w)] for i in range(h)]
                        return out
    return []