def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                if i + 1 < h and j + 1 < w and grid[i + 1][j + 1] == 5 and (i == 0 or j == 0 or grid[i - 1][j - 1] != 5):
                    cnt += 1
                if i + 1 < h and j - 1 >= 0 and grid[i + 1][j - 1] == 5 and (i == 0 or j == w - 1 or grid[i - 1][j + 1] != 5):
                    cnt += 1
    return [[0] for _ in range(cnt)]