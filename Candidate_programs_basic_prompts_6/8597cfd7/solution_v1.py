def solve(grid):
    n = len(grid)
    m = len(grid[0])
    grey_row = next(i for i,row in enumerate(grid) if all(c==5 for c in row))
    colors = {c for row in grid for c in row if c not in (0,5)}
    colors = sorted(colors)
    best = None
    best_diff = -1
    for c in colors:
        above = sum(grid[i][j]==c for i in range(grey_row) for j in range(m))
        below = sum(grid[i][j]==c for i in range(grey_row+1,n) for j in range(m))
        diff = abs(below-above)
        if diff>best_diff:
            best_diff = diff
            best = c
    return [[best,best],[best,best]]