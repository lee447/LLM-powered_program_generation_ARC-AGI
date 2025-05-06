def solve(grid):
    n = len(grid)
    sep = [i for i in range(n) if all(grid[i][j] == 0 for j in range(n))]
    bs = sep[1] - sep[0] - 1
    out = [row[:] for row in grid]
    for bi, r0 in enumerate(sep[:-1]):
        for bj, c0 in enumerate(sep[:-1]):
            r0 += 1
            c0 = sep[bj] + 1
            block = [grid[r][c0:c0+bs] for r in range(r0, r0+bs)]
            colors = set(x for row in block for x in row if x)
            if len(colors) == 2:
                a, b = sorted(colors)
            else:
                continue
            for i in range(bs):
                for j in range(bs):
                    if block[i][j] == a:
                        if bs//2 - i <= j - bs//2 and bs//2 - j <= i - bs//2:
                            out[r0+i][c0+j] = b
                    if block[i][j] == b:
                        if not (bs//2 - i <= j - bs//2 and bs//2 - j <= i - bs//2):
                            out[r0+i][c0+j] = a
    return out