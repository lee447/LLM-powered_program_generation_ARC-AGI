def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    res = [row[:] for row in grid]
    seen = set()
    for i in range(h):
        for j in range(w):
            k = orig[i][j]
            if k <= 1: continue
            cmin = j
            while cmin > 0 and orig[i][cmin-1] in (1, k):
                cmin -= 1
            cmax = j
            while cmax < w-1 and orig[i][cmax+1] in (1, k):
                cmax += 1
            rmin = i
            while rmin > 0 and orig[rmin-1][j] in (1, k):
                rmin -= 1
            rmax = i
            while rmax < h-1 and orig[rmax+1][j] in (1, k):
                rmax += 1
            if rmax - rmin < 2 or cmax - cmin < 2: continue
            key = (rmin, rmax, cmin, cmax)
            if key in seen: continue
            seen.add(key)
            for r in range(rmin+1, rmax):
                for c in range(cmin+1, cmax):
                    if orig[r][c] == 1:
                        res[r][c] = k
    return res