def solve(grid):
    ev = [i for i in range(len(grid[0])) if grid[0][i] == 2 or grid[1][i] == 2]
    h = len(ev)
    w = h - 1
    out = [[0]*w for _ in range(h)]
    mid = w//2
    out[0][mid] = 3
    x = mid
    for j in range(1, h):
        i = ev[j]
        top = grid[0][i] == 2
        bot = grid[1][i] == 2
        if top and bot:
            out[j][x] = 2
            out[j][x+1] = 2
            x += 1
        elif bot:
            out[j][x] = 2
            out[j][x+1] = 2
        else:
            out[j][x] = 2
    return out