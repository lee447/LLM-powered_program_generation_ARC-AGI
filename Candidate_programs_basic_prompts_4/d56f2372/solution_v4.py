def solve(grid):
    h, w = len(grid), len(grid[0])
    found = False
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                c = grid[i][j]
                found = True
                break
        if found:
            break
    minr, maxr, minc, maxc = h, -1, w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == c:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    sub = [[grid[i][j] for j in range(minc, maxc+1)] for i in range(minr, maxr+1)]
    H = len(sub); W = len(sub[0])
    mid = W // 2
    if sub[0][mid] != 0:
        r = H - 1
        H2 = 2*r + 1
        W2 = 2*r + 1
        out = [[0]*W2 for _ in range(H2)]
        cx = cy = r
        for y in range(H2):
            for x in range(W2):
                if abs(y-cy) + abs(x-cx) == r:
                    out[y][x] = 1
        return out
    return sub