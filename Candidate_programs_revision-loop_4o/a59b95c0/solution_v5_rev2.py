def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        row = grid[i] * (n if n == m else 2)
        for _ in range(2):
            result.append(row)
    return result