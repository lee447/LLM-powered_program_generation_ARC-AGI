def solve(grid):
    h, w = len(grid), len(grid[0])
    col = 6
    minr, maxr, minc, maxc = h, -1, w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == col:
                minr = min(minr, r); maxr = max(maxr, r)
                minc = min(minc, c); maxc = max(maxc, c)
    neigh = []
    for c in range(minc, maxc+1):
        if minr-1 >= 0: neigh.append(grid[minr-1][c])
        if maxr+1 < h: neigh.append(grid[maxr+1][c])
    for r in range(minr, maxr+1):
        if minc-1 >= 0: neigh.append(grid[r][minc-1])
        if maxc+1 < w: neigh.append(grid[r][maxc+1])
    if not neigh: return grid
    uniq = sorted(set(neigh))
    a, b = uniq[0], uniq[-1]
    c = uniq[len(uniq)//2]
    res = [row[:] for row in grid]
    H = maxr - minr
    W = maxc - minc
    for r in range(minr, maxr+1):
        for cc in range(minc, maxc+1):
            if grid[r][cc] == col:
                i = (r - minr) / H if H else 0
                j = (cc - minc) / W if W else 0
                s = i + j
                if s < 0.5:
                    res[r][cc] = c
                elif s > H/W * 1.5 if W else s > 1.5:
                    res[r][cc] = b
                else:
                    res[r][cc] = a
    return res