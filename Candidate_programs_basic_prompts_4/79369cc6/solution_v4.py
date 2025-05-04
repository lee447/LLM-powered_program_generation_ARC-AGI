def solve(grid):
    R, C = len(grid), len(grid[0])
    marker = 4
    pts = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == marker]
    minr = min(i for i, j in pts)
    maxr = max(i for i, j in pts)
    minc = min(j for i, j in pts)
    maxc = max(j for i, j in pts)
    h, w = maxr - minr + 1, maxc - minc + 1
    pat = [row[minc:minc+w] for row in grid[minr:minr+h]]
    def trans(p, t):
        if t == 0:
            return p, (h, w)
        if t == 1:
            return [[p[h-1-i][w-1-j] for j in range(w)] for i in range(h)], (h, w)
        if t == 2:
            return [[p[i][w-1-j] for j in range(w)] for i in range(h)], (h, w)
        if t == 3:
            return [[p[h-1-i][j] for j in range(w)] for i in range(h)], (h, w)
        if t == 4:
            return [[p[h-1-j][i] for j in range(h)] for i in range(w)], (w, h)
        if t == 5:
            return [[p[j][i] for j in range(h)] for i in range(w)], (w, h)
        if t == 6:
            return [[p[w-1-j][h-1-i] for j in range(h)] for i in range(w)], (w, h)
        if t == 7:
            return [[p[j][h-1-i] for j in range(h)] for i in range(w)], (w, h)
    res = [row[:] for row in grid]
    for t in range(1, 8):
        pat_t, (h2, w2) = trans(pat, t)
        for i in range(R - h2 + 1):
            for j in range(C - w2 + 1):
                if t == 0 and i == minr and j == minc:
                    continue
                ok = True
                for ii in range(h2):
                    for jj in range(w2):
                        v = pat_t[ii][jj]
                        g = res[i+ii][j+jj]
                        if v == marker:
                            if g == marker:
                                ok = False
                                break
                        else:
                            if g != v:
                                ok = False
                                break
                    if not ok:
                        break
                if ok:
                    for ii in range(h2):
                        for jj in range(w2):
                            if pat_t[ii][jj] == marker:
                                res[i+ii][j+jj] = marker
    return res