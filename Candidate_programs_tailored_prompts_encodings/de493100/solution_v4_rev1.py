def solve(grid):
    H, W = len(grid), len(grid[0])
    rmin, rmax, cmin, cmax = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 7:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    h, w = rmax - rmin + 1, cmax - cmin + 1
    best, best9 = None, float('inf')
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            cnt7 = False
            cnt9 = 0
            for ii in range(i, i + h):
                for jj in range(j, j + w):
                    v = grid[ii][jj]
                    if v == 7:
                        cnt7 = True
                        break
                    if v == 9:
                        cnt9 += 1
                if cnt7:
                    break
            if not cnt7 and cnt9 < best9:
                best9 = cnt9
                best = (i, j)
    i0, j0 = best
    return [row[j0:j0 + w] for row in grid[i0:i0 + h]]