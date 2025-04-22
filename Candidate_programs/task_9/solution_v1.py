def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [[0] * w for _ in range(h)]
    for b in range(w // 3):
        bc = b * 3
        ps = [(r, c - bc) for r in range(h) for c in range(bc, bc + 3) if grid[r][c] == 5]
        if len(ps) == 8:
            color = 3
        elif ps == [(1, 1)]:
            color = 4
        elif ps == [(0, 0), (0, 1), (0, 2)]:
            color = 6
        elif ps == [(2, 0), (2, 1), (2, 2)]:
            color = 1
        elif ps == [(0, 2), (1, 1), (2, 0)]:
            color = 9
        else:
            color = 0
        for r in range(h):
            for c in range(bc, bc + 3):
                out[r][c] = color
    return out