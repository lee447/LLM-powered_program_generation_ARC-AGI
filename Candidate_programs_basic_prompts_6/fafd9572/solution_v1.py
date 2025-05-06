def solve(grid):
    R, C = len(grid), len(grid[0])
    seed3 = None
    for i in range(R - 2):
        for j in range(C - 2):
            cnt_non = cnt_one = 0
            for di in range(3):
                for dj in range(3):
                    v = grid[i+di][j+dj]
                    if v == 1:
                        cnt_one += 1
                    elif v != 0:
                        cnt_non += 1
            if cnt_one == 0 and cnt_non == 6:
                seed3 = (i, j)
                diag = grid[i][j]
                off = grid[i][j+1]
                break
        if seed3: break
    if seed3:
        si, sj = seed3
        for i in range(R - 2):
            for j in range(C - 2):
                cnt_non = cnt_one = 0
                for di in range(3):
                    for dj in range(3):
                        v = grid[i+di][j+dj]
                        if v == 1:
                            cnt_one += 1
                        elif v != 0:
                            cnt_non += 1
                if cnt_one == 6 and cnt_non == 0:
                    rb, cb = i // 4, j // 4
                    nc = diag if rb == cb else off
                    for di, dj in ((0,0),(0,1),(1,0),(1,2),(2,1),(2,2)):
                        if grid[i+di][j+dj] == 1:
                            grid[i+di][j+dj] = nc
        return grid
    seed2 = None
    for i in range(R - 1):
        for j in range(C - 1):
            cnt_non = cnt_one = 0
            for di in range(2):
                for dj in range(2):
                    v = grid[i+di][j+dj]
                    if v == 1:
                        cnt_one += 1
                    elif v != 0:
                        cnt_non += 1
            if cnt_one == 0 and cnt_non >= 3:
                seed2 = (i, j)
                break
        if seed2: break
    si, sj = seed2
    sv = [[grid[si][sj], grid[si][sj+1]], [grid[si+1][sj], grid[si+1][sj+1]]]
    sb = sj // 4
    rel = [(0,0),(0,1),(1,0)]
    for i in range(R - 1):
        for j in range(C - 1):
            if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j] == 1 and grid[i+1][j+1] == 0:
                cb = j // 4
                off = cb - sb - 1
                if 0 <= off < 2:
                    nc = sv[0][off] if i < si else sv[1][off]
                    for di, dj in rel:
                        if grid[i+di][j+dj] == 1:
                            grid[i+di][j+dj] = nc
    return grid