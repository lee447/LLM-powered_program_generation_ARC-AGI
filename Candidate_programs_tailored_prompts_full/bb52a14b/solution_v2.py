def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    fills = []
    for r in range(h - 2):
        for c in range(w - 2):
            has1 = has8 = has4 = False
            for i in range(3):
                for j in range(3):
                    v = grid[r + i][c + j]
                    if v == 1: has1 = True
                    elif v == 8: has8 = True
                    elif v == 4: has4 = True
            if has1 and has8 and not has4:
                fills.append((r, c))
    for r, c in fills:
        for i in range(3):
            for j in range(3):
                if out[r + i][c + j] == 0:
                    out[r + i][c + j] = 4
    return out