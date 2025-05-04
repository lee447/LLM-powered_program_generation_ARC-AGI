def solve(grid):
    n = len(grid[0])
    c = n // 2
    row_start = 3
    out = [[0]*n for _ in range(n)]
    for i in range(c+1):
        j1 = c - i
        j2 = c + i
        if 0 <= j1 < n: out[i][j1] = 2
        if 0 <= j2 < n: out[i][j2] = 2
    k0 = (c - 1) - row_start
    k_list = []
    l = 0
    while True:
        k = k0 - 4*l
        if k <= -n or k >= n: break
        k_list.append(k)
        l += 1
    for idx, k in enumerate(k_list):
        start_i = row_start + 2*idx
        for i in range(start_i, n):
            j = i + k
            if 0 <= j < n:
                out[i][j] = 1
    return out