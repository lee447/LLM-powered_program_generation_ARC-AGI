def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    expand = {2:2, 4:2, 3:3, 6:3}
    for i in range(1, h-1):
        for j in range(1, w-1):
            c = grid[i][j]
            if c in expand:
                ok = True
                for di in (-1,0,1):
                    for dj in (-1,0,1):
                        if di==0 and dj==0: continue
                        if grid[i+di][j+dj] != 1:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    s = expand[c]
                    if s % 2:
                        rs = - (s//2)
                        cs = - (s//2)
                    else:
                        rs = 0
                        cs = - (s//2)
                    for di in range(rs, rs+s):
                        for dj in range(cs, cs+s):
                            res[i+di][j+dj] = c
    return res