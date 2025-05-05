def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    (r1, c1), (r2, c2) = pts
    dr, dc = r2 - r1, c2 - c1
    steps = max(abs(dr), abs(dc))
    sr, sc = dr // steps, dc // steps
    out = [row[:] for row in grid]
    for i in range(steps + 1):
        r, c = r1 + sr * i, c1 + sc * i
        if grid[r][c] == 2:
            out[r][c] = 2
        elif grid[r][c] == 1:
            out[r][c] = 3
        else:
            out[r][c] = 2
    return out