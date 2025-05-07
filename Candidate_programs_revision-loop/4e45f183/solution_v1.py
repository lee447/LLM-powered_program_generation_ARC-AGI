def solve(grid):
    n = len(grid)
    bs = (n - 4) // 3
    step = bs + 1
    cols = sorted({v for row in grid for v in row if v != 0})
    c1, c2 = cols[0], cols[1]
    plus_shape = plus_back = L_shape = L_back = None
    for bi in range(3):
        for bj in range(3):
            top = 1 + bi * step
            left = 1 + bj * step
            cnt1 = cnt2 = 0
            for i in range(bs):
                for j in range(bs):
                    v = grid[top + i][left + j]
                    if v == c1: cnt1 += 1
                    elif v == c2: cnt2 += 1
            if plus_shape is None and (cnt1 == 2 * bs - 1 or cnt2 == 2 * bs - 1):
                if cnt1 == 2 * bs - 1:
                    plus_shape, plus_back = c1, c2
                else:
                    plus_shape, plus_back = c2, c1
            if L_shape is None and (cnt1 == 3 or cnt2 == 3):
                if cnt1 == 3:
                    L_shape, L_back = c1, c2
                else:
                    L_shape, L_back = c2, c1
    out = [[0] * n for _ in range(n)]
    for bi in range(3):
        for bj in range(3):
            top = 1 + bi * step
            left = 1 + bj * step
            if bi == 1 or bj == 1:
                for i in range(bs):
                    for j in range(bs):
                        out[top + i][left + j] = plus_back
                mid = bs // 2
                for k in range(bs):
                    out[top + mid][left + k] = plus_shape
                    out[top + k][left + mid] = plus_shape
            else:
                for i in range(bs):
                    for j in range(bs):
                        out[top + i][left + j] = L_back
                if bi == 0 and bj == 0:
                    pts = [(0, 0), (0, 1), (1, 0)]
                elif bi == 0 and bj == 2:
                    pts = [(0, bs - 1), (0, bs - 2), (1, bs - 1)]
                elif bi == 2 and bj == 0:
                    pts = [(bs - 1, 0), (bs - 1, 1), (bs - 2, 0)]
                else:
                    pts = [(bs - 1, bs - 1), (bs - 1, bs - 2), (bs - 2, bs - 1)]
                for dx, dy in pts:
                    out[top + dx][left + dy] = L_shape
    return out