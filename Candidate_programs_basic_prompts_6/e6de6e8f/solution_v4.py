def solve(grid):
    r0, r1 = grid
    n = len(r0)
    sep = [i for i in range(n) if r0[i] == 2 and r1[i] == 2]
    non = [i for i in range(n) if not (r0[i] == 2 and r1[i] == 2)]
    m = len(non)
    leaves = [non.index(i) for i in range(n) if r1[i] == 2 and r0[i] != 2]
    import math
    cx = math.ceil(sum(leaves) / len(leaves)) + 1
    h = m + 1
    out = [[0] * m for _ in range(h)]
    out[0][cx] = 3
    left = [x for x in leaves if x < cx]
    right = [x for x in leaves if x > cx]
    if len(left) > len(right):
        for y in (1,2):
            for x in range(cx - len(left), cx + 1):
                out[y][x] = 2
        y0 = 3
        for x in range(cx - len(left) + 1, cx + 1):
            out[y0][x] = 2
        for y in range(y0 + 1, h):
            out[y][cx - len(left) + 1] = 2
    else:
        for y in (1,2):
            for x in range(cx, cx + len(right) + 1):
                out[y][x] = 2
        y0 = 3
        for x in range(cx, cx + len(right)):
            out[y0][x] = 2
        for y in range(y0 + 1, h):
            out[y][cx + len(right) - 1] = 2
    return out