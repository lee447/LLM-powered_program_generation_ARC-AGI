def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    max_gap = 3
    for i in range(h):
        nz = [j for j in range(w) if grid[i][j] in (1,8)]
        for a in range(len(nz)):
            for b in range(a+1, len(nz)):
                j, k = nz[a], nz[b]
                if 1 <= k-j <= max_gap and grid[i][j] != grid[i][k]:
                    for t in range(j+1, k):
                        if res[i][t] == 0:
                            res[i][t] = 4
    for i in range(h):
        nz = [j for j in range(w) if grid[i][j] in (1,8)]
        for j in nz:
            left = any(abs(j-k) <= max_gap for k in nz if k != j)
            if not left:
                if j-1 >= 0 and res[i][j-1] == 0:
                    res[i][j-1] = 4
                if j+1 < w and res[i][j+1] == 0:
                    res[i][j+1] = 4
    patterns = [
        ((0,1,8),(1,0,8),(1,2,1)),
        ((1,0,8),(2,1,8),(0,1,1)),
        ((1,0,1),(0,1,8),(1,2,8)),
        ((0,1,1),(1,2,8),(2,1,8))
    ]
    for i in range(h-2):
        for j in range(w-2):
            block = [res[i+di][j+dj] for di in range(3) for dj in range(3)]
            for pat in patterns:
                ok = True
                for di, dj, v in pat:
                    if grid[i+di][j+dj] != v:
                        ok = False
                        break
                if not ok:
                    continue
                # check no other nonzero in input block
                for di in range(3):
                    for dj in range(3):
                        if (di,dj,v) not in [(x,y,z) for x,y,z in pat]:
                            if grid[i+di][j+dj] != 0:
                                ok = False
                                break
                    if not ok:
                        break
                if not ok:
                    continue
                for di in range(3):
                    for dj in range(3):
                        if res[i+di][j+dj] == 0:
                            res[i+di][j+dj] = 4
    return res