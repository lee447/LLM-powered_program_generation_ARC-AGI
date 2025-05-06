def solve(grid):
    h = len(grid)
    w = len(grid[0])
    B = None
    orig = None
    for i in range(h-2):
        for j in range(w-2):
            ok = True
            for di in range(3):
                for dj in range(3):
                    if grid[i+di][j+dj] == 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                B = [row[j:j+3] for row in grid[i:i+3]]
                orig = (i, j)
                break
        if B is not None:
            break
    out = [row[:] for row in grid]
    for i in range(h-2):
        for j in range(w-2):
            if orig is not None and (i, j) == orig:
                continue
            matches = mism = nonz = 0
            for di in range(3):
                for dj in range(3):
                    v = grid[i+di][j+dj]
                    if v != 0:
                        nonz += 1
                        if v == B[di][dj]:
                            matches += 1
                        else:
                            mism += 1
            cond = False
            if nonz == 0:
                cond = True
            elif matches >= 3 and mism == 0:
                cond = True
            elif matches >= 2 and mism <= 1:
                cond = True
            if cond:
                for di in range(3):
                    for dj in range(3):
                        out[i+di][j+dj] = B[di][dj]
    return out