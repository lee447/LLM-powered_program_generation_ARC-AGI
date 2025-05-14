def solve(grid):
    result = [[0] * len(grid[0]) for _ in range(3)]
    for i in range(len(grid)):
        if any(cell != 0 for cell in grid[i]):
            result[1] = grid[i]
            break
    return result