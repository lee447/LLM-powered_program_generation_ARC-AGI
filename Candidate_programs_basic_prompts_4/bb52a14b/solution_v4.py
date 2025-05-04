def solve(grid):
    h, w = len(grid), len(grid[0])
    tmpl = None
    for i in range(h - 2):
        for j in range(w - 2):
            sub = [grid[i + di][j + dj] for di in range(3) for dj in range(3)]
            if all(v != 0 for v in sub):
                tmpl = [[grid[i+di][j+dj] for dj in range(3)] for di in range(3)]
                ti, tj = i+1, j+1
                break
        if tmpl: break
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if grid[i][j] != tmpl[1][1]: continue
            zeros = False
            ok = True
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    v = grid[i+di][j+dj]
                    tv = tmpl[di+1][dj+1]
                    if v == 0:
                        zeros = True
                    elif v != tv:
                        ok = False
                        break
                if not ok: break
            if ok and zeros and not (i == ti and j == tj):
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if grid[i+di][j+dj] == 0:
                            grid[i+di][j+dj] = tmpl[di+1][dj+1]
    return grid