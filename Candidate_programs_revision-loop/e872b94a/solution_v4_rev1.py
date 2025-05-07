def solve(grid):
    h = len(grid)
    if h == 0:
        return []
    w = len(grid[0])
    max_len = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                if i - 1 < 0 or j - 1 < 0 or grid[i-1][j-1] != 5:
                    x, y, l = i, j, 0
                    while x < h and y < w and grid[x][y] == 5:
                        l += 1
                        x += 1
                        y += 1
                    if l > max_len:
                        max_len = l
                if i - 1 < 0 or j + 1 >= w or grid[i-1][j+1] != 5:
                    x, y, l = i, j, 0
                    while x < h and y >= 0 and grid[x][y] == 5:
                        l += 1
                        x += 1
                        y -= 1
                    if l > max_len:
                        max_len = l
    return [[0] for _ in range(max_len)]