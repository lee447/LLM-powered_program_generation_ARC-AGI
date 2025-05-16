def solve(grid):
    m, n = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    sep = n
    for j in range(n):
        col = [grid[i][j] for i in range(m)]
        if all(c == col[0] and c != bg for c in col):
            sep = j
            break
    return [row[:sep] for row in grid]