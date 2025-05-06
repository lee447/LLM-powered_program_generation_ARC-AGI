def solve(grid):
    row1, row2 = grid
    n = len(row1)
    or_idx = [i for i in range(n) if row1[i] or row2[i]]
    codes = [(1 if row1[i] else 0) + (2 if row2[i] else 0) for i in or_idx]
    total = len(codes)
    out = [[0]*7 for _ in range(total)]
    out[0][3] = 3
    x = 3
    for k in range(1, total):
        c = codes[k-1]
        if c == 1:
            x += 1
            L = 1
        elif c == 2:
            L = 1
        else:
            if k < total//2 + total%2:
                L = 2
            else:
                L = 1
        for j in range(L):
            xx = min(6, x + j)
            out[k][xx] = 2
    return out