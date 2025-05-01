def solve(grid: list[list[int]]) -> list[list[int]]:
    n, m = len(grid), len(grid[0])
    ones = sorted((r, c) for r in range(n) for c in range(m) if grid[r][c] == 1)
    (r0, c0), (r1, c1), (r2, c2) = ones
    dr, dc = r1 - r0, c1 - c0
    r, c = r2, c2
    while True:
        r += dr
        c += dc
        if not (0 <= r < n and 0 <= c < m):
            break
        grid[r][c] = 2
    return grid