def solve(grid):
    h = len(grid)
    w = len(grid[0])
    max_run = 0
    bar_color = None
    bar_row = -1
    bar_end = -1
    for i in range(h):
        j = 0
        while j < w:
            c = grid[i][j]
            if c != 0:
                k = j + 1
                while k < w and grid[i][k] == c:
                    k += 1
                run = k - j
                if run > max_run:
                    max_run = run
                    bar_color = c
                    bar_row = i
                    bar_end = k - 1
                j = k
            else:
                j += 1
    target = None
    for i in range(bar_row):
        for j in range(bar_end + 1):
            c = grid[i][j]
            if c != 0 and c != bar_color:
                target = c
                break
        if target is not None:
            break
    return [[c if c != target else 0 for c in row] for row in grid]