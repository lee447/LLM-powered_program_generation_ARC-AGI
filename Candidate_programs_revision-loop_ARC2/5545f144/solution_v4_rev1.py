def solve(grid):
    m, n = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    seps = [j for j in range(n) if all(grid[i][j] == grid[0][j] != bg for i in range(m))]
    first_sep = seps[0]
    return [row[:first_sep] for row in grid]