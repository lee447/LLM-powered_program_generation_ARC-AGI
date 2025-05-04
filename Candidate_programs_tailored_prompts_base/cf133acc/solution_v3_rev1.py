def solve(grid: list[list[int]]) -> list[list[int]]:
    H = len(grid)
    W = len(grid[0])
    shapes = []
    for y in range(H):
        d = {}
        for x in range(W):
            c = grid[y][x]
            if c != 0:
                d.setdefault(c, []).append(x)
        for c, cols in d.items():
            cols.sort()
            runs = []
            curr = [cols[0]]
            for x in cols[1:]:
                if x == curr[-1] + 1:
                    curr.append(x)
                else:
                    runs.append(curr)
                    curr = [x]
            runs.append(curr)
            if len(runs) == 2 and runs[1][0] - runs[0][-1] == 2:
                l = runs[0][0]
                r = runs[1][-1]
                g = runs[0][-1] + 1
                shapes.append((y, l, r, g, c))
    shapes.sort(key=lambda t: t[0])
    out = [row[:] for row in grid]
    for y, l, r, g, c in shapes:
        for x in range(l, r + 1):
            out[y][x] = c
        for yy in range(y - 1, -1, -1):
            if out[yy][g] == 0:
                out[yy][g] = c
            else:
                break
    return out