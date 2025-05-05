def solve(grid):
    m, n = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    out = [row[:] for row in grid]
    for k in range(min(m, n), 2, -1):
        for r in range(m - k + 1):
            for c in range(n - k + 1):
                ok = True
                for i in range(k):
                    if orig[r][c + i] != 1 or orig[r + k - 1][c + i] != 1 or orig[r + i][c] != 1 or orig[r + i][c + k - 1] != 1:
                        ok = False
                        break
                if not ok:
                    continue
                anchors = set()
                for i in range(1, k - 1):
                    for j in range(1, k - 1):
                        v = orig[r + i][c + j]
                        if v not in (0, 1):
                            anchors.add(v)
                if len(anchors) == 1:
                    a = anchors.pop()
                    for i in range(1, k - 1):
                        for j in range(1, k - 1):
                            out[r + i][c + j] = a
    return out