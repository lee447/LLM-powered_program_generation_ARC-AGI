def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_col = None
    for c in range(w):
        v = grid[0][c]
        pure = True
        for r in range(h):
            if grid[r][c] != v:
                pure = False
                break
        if pure and v in (1, 7):
            sep_col = c
            break
    if sep_col is not None:
        grid = [row[:sep_col] for row in grid]
        h, w = len(grid), len(grid[0])
    new = []
    for r in range(h):
        v = grid[r][0]
        pure = True
        for c in range(w):
            if grid[r][c] != v:
                pure = False
                break
        if not (pure and v in (1, 7)):
            new.append(grid[r])
    grid = new
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 7:
                grid[r][c] = 4
    return grid