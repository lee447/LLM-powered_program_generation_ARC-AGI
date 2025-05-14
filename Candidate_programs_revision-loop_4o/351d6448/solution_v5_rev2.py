def solve(grid):
    result = [[0] * len(grid[0]) for _ in range(3)]
    for i in range(len(grid) - 1, -1, -1):
        if any(cell != 0 for cell in grid[i]):
            result[1] = grid[i]
            break
    for i in range(len(grid) - 1, -1, -1):
        if any(cell != 0 for cell in grid[i]) and grid[i] != result[1]:
            result[1] = grid[i]
            break
    return result