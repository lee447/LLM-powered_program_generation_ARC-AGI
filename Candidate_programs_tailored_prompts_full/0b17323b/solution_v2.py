def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    n = min(h, w)
    blues = [i for i in range(n) if grid[i][i] == 1]
    if len(blues) < 2:
        return [row[:] for row in grid]
    step = blues[1] - blues[0]
    new = [row[:] for row in grid]
    nxt = blues[-1] + step
    while nxt < n:
        new[nxt][nxt] = 2
        nxt += step
    return new