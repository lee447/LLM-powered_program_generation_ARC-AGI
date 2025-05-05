def solve(grid):
    R, C = len(grid), len(grid[0])
    r0, c0 = R, C
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 8:
                if i < r0: r0 = i
                if j < c0: c0 = j
    h = 0
    while r0 + h < R and grid[r0 + h][c0] == 8:
        h += 1
    w = 0
    while c0 + w < C and grid[r0][c0 + w] == 8:
        w += 1
    for i in range(R):
        for j in range(C):
            if i + h < R and j + w < C and grid[i][j] == 5:
                ok = True
                for k in range(w):
                    if grid[i][j + k] != 5:
                        ok = False
                        break
                if not ok:
                    continue
                for l in range(h):
                    if grid[i + l][j] != 5:
                        ok = False
                        break
                if ok:
                    out = []
                    for ii in range(i + 1, i + 1 + h):
                        out.append(grid[ii][j + 1:j + 1 + w])
                    return out