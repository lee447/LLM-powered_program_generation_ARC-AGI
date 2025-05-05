def solve(grid):
    h, w = len(grid), len(grid[0])
    period = 6
    s = 0
    for start in range(0, h - period + 1):
        ok = True
        for dr in range(period):
            row = grid[start + dr]
            for v in row:
                if v == 0:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            s = start
            break
    template = [grid[s + dr] for dr in range(period)]
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if out[r][c] == 0:
                tr = (r - s) % period
                out[r][c] = template[tr][c]
    return out