def solve(grid):
    h = len(grid)
    w = len(grid[0])
    div = next(j for j in range(w) if any(grid[i][j] == 5 for i in range(h)))
    left = [row[:div] for row in grid]
    right = [row[div+1:] for row in grid]
    hh = h
    ww = len(left[0])
    full = True
    for i in range(hh):
        for j in range(ww):
            if left[i][j] == 0 and right[i][j] == 0:
                full = False
                break
        if not full:
            break
    if full:
        return [[left[i][j] if left[i][j] != 0 else right[i][j] for j in range(ww)] for i in range(hh)]
    else:
        return [row[:] for row in left]