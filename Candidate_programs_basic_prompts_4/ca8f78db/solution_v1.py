def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripe_rows = [i for i in range(1, h, 2)]
    best = None
    for i in stripe_rows:
        if 0 not in grid[i]:
            best = i
            break
    if best is None:
        best = min(stripe_rows, key=lambda i: grid[i].count(0))
    S = grid[best]
    for p in range(1, w + 1):
        ok = True
        for j in range(w):
            if S[j] != S[j % p]:
                ok = False
                break
        if ok:
            period = p
            break
    pattern = S[:period]
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                out[i][j] = 1
        else:
            for j in range(w):
                out[i][j] = pattern[j % period]
    return out