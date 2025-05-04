def solve(grid):
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0:
                counts[v] = counts.get(v, 0) + 1
    single_color = next(c for c, cnt in counts.items() if cnt == 1)
    big_color = next(c for c in counts if c != single_color)
    br = bc = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == single_color:
                br, bc = i, j
    minr = min(i for i in range(h) for j in range(w) if grid[i][j] == big_color)
    maxr = max(i for i in range(h) for j in range(w) if grid[i][j] == big_color)
    minc = min(j for i in range(h) for j in range(w) if grid[i][j] == big_color)
    maxc = max(j for i in range(h) for j in range(w) if grid[i][j] == big_color)
    Mh = maxr - minr + 1
    Mw = maxc - minc + 1
    M = [[1 if grid[minr + i][minc + j] == big_color else 0 for j in range(Mw)] for i in range(Mh)]
    def flip_h(m):
        return [row[::-1] for row in m]
    def flip_v(m):
        return m[::-1]
    orientations = [M, flip_h(M), flip_v(M), flip_v(flip_h(M))]
    res = [row[:] for row in grid]
    for M0 in orientations:
        Mh0 = len(M0)
        Mw0 = len(M0[0])
        ones = [(i, j) for i in range(Mh0) for j in range(Mw0) if M0[i][j]]
        for pr, pc in ones:
            sr = br - pr
            sc = bc - pc
            ok = True
            for i, j in ones:
                x = sr + i
                y = sc + j
                if x < 0 or x >= h or y < 0 or y >= w:
                    ok = False; break
                v = grid[x][y]
                if v != 0 and v != single_color:
                    ok = False; break
            if not ok:
                continue
            # apply
            for i, j in ones:
                x = sr + i
                y = sc + j
                res[x][y] = single_color
            for i in range(h):
                for j in range(w):
                    if grid[i][j] == big_color:
                        res[i][j] = big_color
            return res
    return grid