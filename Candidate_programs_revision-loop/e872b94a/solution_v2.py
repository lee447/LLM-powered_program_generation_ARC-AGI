def solve(grid):
    h, w = len(grid), len(grid[0]) if grid else 0
    max_len = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                l = 0
                x, y = i, j
                while x < h and y < w and grid[x][y] == 5:
                    l += 1
                    x += 1
                    y += 1
                if l > max_len: max_len = l
                l = 0
                x, y = i, j
                while x < h and y >= 0 and grid[x][y] == 5:
                    l += 1
                    x += 1
                    y -= 1
                if l > max_len: max_len = l
    return [[0] for _ in range(max_len)]