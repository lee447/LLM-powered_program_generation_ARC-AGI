def solve(grid):
    h = len(grid)
    w = len(grid[0])
    n = min(h, w)
    cnt = 0
    for i in range(n):
        if grid[i][i] == 5:
            cnt += 1
    return [[0] for _ in range(cnt)]