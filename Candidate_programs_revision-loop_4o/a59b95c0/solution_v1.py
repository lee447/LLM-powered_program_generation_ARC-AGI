def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        row = grid[i] * (n if n == m else 3)
        for _ in range(n if n == m else 3):
            result.append(row)
    return result