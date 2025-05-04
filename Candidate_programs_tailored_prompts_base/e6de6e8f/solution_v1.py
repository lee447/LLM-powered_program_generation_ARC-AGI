def solve(grid):
    pairs = [c for c in range(len(grid[0])) if grid[0][c] == 2 and grid[1][c] == 2]
    n = len(pairs)
    h = 2 * n + 1
    w = n + 3
    out = [[0] * w for _ in range(h)]
    out[0][3] = 3
    for i in range(n):
        r = 1 + 2 * i
        c0 = 3 + i
        for dr in (0, 1):
            for dc in (0, 1):
                rr = r + dr
                cc = c0 + dc
                if 0 <= rr < h and 0 <= cc < w:
                    out[rr][cc] = 2
    return out