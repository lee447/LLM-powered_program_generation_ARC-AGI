def solve(grid):
    R = len(grid)
    C = len(grid[0])
    w = C // 3
    res = [[0]*C for _ in range(R)]
    fills = []
    for b in range(3):
        coords = []
        for r in range(R):
            for c in range(b*w, (b+1)*w):
                if grid[r][c] == 5:
                    coords.append((r, c))
        if len(coords) == 1:
            fill = 4
        elif len(coords) == 8:
            fill = 3
        elif len(coords) == 3:
            rows = [r for r, _ in coords]
            if len(set(rows)) == 1:
                if rows[0] == 0:
                    fill = 6
                else:
                    fill = 1
            else:
                fill = 9
        else:
            fill = 0
        fills.append(fill)
    for b in range(3):
        f = fills[b]
        for r in range(R):
            for c in range(b*w, (b+1)*w):
                res[r][c] = f
    return res