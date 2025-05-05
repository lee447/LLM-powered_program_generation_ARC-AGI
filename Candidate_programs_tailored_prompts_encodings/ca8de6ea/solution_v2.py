def solve(grid):
    n = len(grid)
    m = n // 2
    o = m + 1
    center_out = o // 2
    out = [[0] * o for _ in range(o)]
    for i in range(n):
        for j in range(n):
            v = grid[i][j]
            if v == 0:
                continue
            di = i - m
            dj = j - m
            if di == 0 and dj == 0:
                oi, oj = center_out, center_out
            elif abs(di) == m and abs(dj) == m:
                oi = (di // m) * center_out + center_out
                oj = (dj // m) * center_out + center_out
            else:
                if di < 0 and dj < 0:
                    oi, oj = 0, center_out
                elif di < 0 and dj > 0:
                    oi, oj = center_out, o - 1
                elif di > 0 and dj < 0:
                    oi, oj = center_out, 0
                else:
                    oi, oj = o - 1, center_out
            out[oi][oj] = v
    return out