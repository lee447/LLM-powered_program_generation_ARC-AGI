def solve(grid):
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    rects = []
    for i1 in range(R):
        for j1 in range(C):
            b = grid[i1][j1]
            if b == 0:
                continue
            for i2 in range(i1+2, R):
                if grid[i2][j1] != b:
                    break
                for j2 in range(j1+2, C):
                    if grid[i1][j2] != b or grid[i2][j2] != b:
                        continue
                    ok = True
                    for jj in range(j1, j2+1):
                        if grid[i1][jj] != b or grid[i2][jj] != b:
                            ok = False
                            break
                    if not ok:
                        continue
                    for ii in range(i1, i2+1):
                        if grid[ii][j1] != b or grid[ii][j2] != b:
                            ok = False
                            break
                    if not ok:
                        continue
                    nonb = set()
                    for ii in range(i1+1, i2):
                        for jj in range(j1+1, j2):
                            v = grid[ii][jj]
                            if v != b:
                                nonb.add(v)
                    if len(nonb) == 1:
                        c = nonb.pop()
                        rects.append((i1, j1, i2, j2, (i2-i1-1)*(j2-j1-1), c))
    rects.sort(key=lambda x: x[4], reverse=True)
    for i1, j1, i2, j2, _, c in rects:
        for ii in range(i1+1, i2):
            for jj in range(j1+1, j2):
                out[ii][jj] = c
    return out