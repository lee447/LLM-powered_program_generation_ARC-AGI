def solve(grid):
    h = len(grid)
    w = len(grid[0])
    uc = [all(grid[i][j] == grid[0][j] for i in range(h)) for j in range(w)]
    ur = [all(grid[i][j] == grid[i][0] for j in range(w)) for i in range(h)]
    vertical = sum(uc) >= sum(ur)
    if vertical:
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
        if runs2:
            run = min(runs2, key=lambda r: r[1] - r[0] + 1)
        else:
            return grid
        wl, wr = run
        cnt = {}
        for i in range(h):
            for j in range(wl):
                cnt[grid[i][j]] = cnt.get(grid[i][j], 0) + 1
        bg = max(cnt, key=cnt.get)
        out = [row[:] for row in grid]
        for i in range(h):
            for j in range(wl):
                v = grid[i][j]
                if v != bg:
                    out[i][j] = bg
                    j2 = wr + wl - j
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
        if runs2:
            run = min(runs2, key=lambda r: r[1] - r[0] + 1)
            tl, br = run
        else:
            top = runs[0][1]
            bot = runs[-1][0]
            length = bot - top - 1
            half = length // 2
            tl = top + 1
            br = top + half
        cnt = {}
        for i in range(tl):
            for j in range(w):
                cnt[grid[i][j]] = cnt.get(grid[i][j], 0) + 1
        bg = max(cnt, key=cnt.get)
        out = [row[:] for row in grid]
        for i in range(tl):
            for j in range(w):
                v = grid[i][j]
                if v != bg:
                    out[i][j] = bg
                    i2 = br + tl - i
                    if 0 <= i2 < h and out[i2][j] == bg:
                        out[i2][j] = v
        return out