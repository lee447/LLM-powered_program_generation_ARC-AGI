def solve(grid):
    x = grid[0].index(2)
    N = 2*x + 1
    out = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            d = abs(r-x) + abs(c-x)
            if d == x and r <= x:
                out[r][c] = 2
            elif d <= x and (c - r) % 4 == x % 4 and c - r < x:
                out[r][c] = 1
    return out