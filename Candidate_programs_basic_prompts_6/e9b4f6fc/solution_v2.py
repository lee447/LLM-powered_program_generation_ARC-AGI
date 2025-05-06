def solve(grid):
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0:
                counts[v] = counts.get(v, 0) + 1
    border = max(counts, key=lambda k: counts[k])
    rmin, rmax, cmin, cmax = h, -1, w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == border:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    mapping = {border: border}
    def outside(i,j):
        return not (rmin <= i <= rmax and cmin <= j <= cmax)
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0 and v != border and outside(i,j):
                for di,dj in ((0,1),(1,0)):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < h and 0 <= nj < w:
                        u = grid[ni][nj]
                        if u != 0 and u != border and outside(ni,nj):
                            mapping[u] = v
    out = []
    for i in range(rmin, rmax+1):
        row = []
        for j in range(cmin, cmax+1):
            row.append(mapping.get(grid[i][j], grid[i][j]))
        out.append(row)
    return out