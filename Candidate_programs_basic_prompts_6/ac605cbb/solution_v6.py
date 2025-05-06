def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    res = [[0]*w for _ in range(h)]
    def draw(r, c, dr, dc, length, color, mark_last):
        r0, c0 = r, c
        for i in range(length):
            r0 += dr; c0 += dc
            res[r0][c0] = 5
        if mark_last:
            r0 += dr; c0 += dc
            res[r0][c0] = color
    if len(pts) == 2:
        (r1, c1, v1), (r2, c2, v2) = pts
        dr = r2 - r1; dc = c2 - c1
        a, b = abs(dr), abs(dc)
        if a >= b:
            sign1 = 1 if dr > 0 else -1
            draw(r1, c1, sign1, 0, a, v1, False)
            sign2 = 1 if dc > 0 else -1
            draw(r1 + sign1*a, c1, 0, sign2, b, v1, True)
        else:
            sign1 = 1 if dc > 0 else -1
            draw(r1, c1, 0, sign1, b, v1, False)
            sign2 = 1 if dr > 0 else -1
            draw(r1, c1 + sign1*b, sign2, 0, a, v1, True)
        dr = r1 - r2; dc = c1 - c2
        a, b = abs(dr), abs(dc)
        if a >= b:
            sign1 = 1 if dr > 0 else -1
            draw(r2, c2, sign1, 0, a, v2, False)
            sign2 = 1 if dc > 0 else -1
            draw(r2 + sign1*a, c2, 0, sign2, b, v2, True)
        else:
            sign1 = 1 if dc > 0 else -1
            draw(r2, c2, 0, sign1, b, v2, False)
            sign2 = 1 if dr > 0 else -1
            draw(r2, c2 + sign1*b, sign2, 0, a, v2, True)
    else:
        for r, c, v in pts:
            res[r][c] = v
    return res