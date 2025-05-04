def solve(grid):
    R = len(grid)
    C = len(grid[0])
    r0, r1, c0, c1 = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    quads = [
        (0, r0 - 1, 0, c0 - 1),
        (0, r0 - 1, c1 + 1, C - 1),
        (r1 + 1, R - 1, 0, c0 - 1),
        (r1 + 1, R - 1, c1 + 1, C - 1),
    ]
    for rr0, rr1, cc0, cc1 in quads:
        if rr1 - rr0 + 1 >= h and cc1 - cc0 + 1 >= w:
            for i in range(rr0, rr1 - h + 2):
                for j in range(cc0, cc1 - w + 2):
                    ok = True
                    for di in range(h):
                        for dj in range(w):
                            if grid[i + di][j + dj] == 0:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        return [grid[i + di][j:j + w] for di in range(h)]
    return []