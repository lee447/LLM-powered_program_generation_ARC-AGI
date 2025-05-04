def solve(grid):
    h = len(grid)
    w = len(grid[0])
    for bi, row in enumerate(grid):
        if all(x == 5 for x in row):
            barrier = bi
            break
    left_col = next(j for j in range(w) for i in range(barrier) if grid[i][j] == 2)
    bottom_left = sum(1 for i in range(barrier + 1, h) if grid[i][left_col] == 2)
    color = 2 if bottom_left >= w // 2 else 4
    return [[color] * 2 for _ in range(2)]