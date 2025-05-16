def solve(grid):
    h = len(grid)
    w = len(grid[0])
    uc = [all(grid[i][j] == grid[0][j] for i in range(h)) for j in range(w)]
    ur = [all(grid[i][j] == grid[i][0] for j in range(w)) for i in range(h)]
    if sum(uc) >= sum(ur):
        runs = []
        j = 0
        while j < w:
            if uc[j]:
                a = j
                while j + 1 < w and uc[j + 1]:
                    j += 1
                runs.append((a, j))
            j += 1
        runs2 = [r for r in runs if r[0] != 0 and r[1] != w - 1]
        if not runs2:
            return grid
        wl, wr = min(runs2, key=lambda r: r[1] - r[0])
        row_start = 0
        while row_start < h and ur[row_start]:
            row_start += 1
        row_end = h - 1
        while row_end >= 0 and ur[row_end]:
            row_end -= 1
        cnt = {}
        for i in range(row_start, row_end + 1):
            for j in range(wl):
                if not uc[j]:
                    cnt[grid[i][j]] = cnt.get(grid[i][j], 0) + 1
        bg = max(cnt, key=cnt.get) if cnt else None
        out = [row[:] for row in grid]
        for i in range(row_start, row_end + 1):
            for j in range(wl):
                if not uc[j]:
                    v = grid[i][j]
                    if v != bg:
                        out[i][j] = bg
                        j2 = wl + wr - j
                        if 0 <= j2 < w and out[i][j2] == bg:
                            out[i][j2] = v
        return out
    else:
        runs = []
        i = 0
        while i < h:
            if ur[i]:
                a = i
                while i + 1 < h and ur[i + 1]:
                    i += 1
                runs.append((a, i))
            i += 1
        runs2 = [r for r in runs if r[0] != 0 and r[1] != h - 1]
        if not runs2:
            return grid
        tl, br = min(runs2, key=lambda r: r[1] - r[0])
        col_start = 0
        while col_start < w and uc[col_start]:
            col_start += 1
        col_end = w - 1
        while col_end >= 0 and uc[col_end]:
            col_end -= 1
        cnt = {}
        for i in range(tl):
            if not ur[i]:
                for j in range(col_start, col_end + 1):
                    cnt[grid[i][j]] = cnt.get(grid[i][j], 0) + 1
        bg = max(cnt, key=cnt.get) if cnt else None
        out = [row[:] for row in grid]
        for i in range(tl):
            if not ur[i]:
                for j in range(col_start, col_end + 1):
                    v = grid[i][j]
                    if v != bg:
                        out[i][j] = bg
                        i2 = tl + br - i
                        if 0 <= i2 < h and out[i2][j] == bg:
                            out[i2][j] = v
        return out