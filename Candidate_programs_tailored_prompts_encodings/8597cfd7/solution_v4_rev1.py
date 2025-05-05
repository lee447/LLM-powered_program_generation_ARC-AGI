def solve(grid):
    rows, cols = len(grid), len(grid[0])
    grey_row = next(i for i, row in enumerate(grid) if all(v == 5 for v in row))
    max_len = grey_row - 1
    stop = min(rows - 1, grey_row + max_len)
    m2 = m4 = 0
    for j in range(cols):
        c2 = c4 = 0
        for i in range(grey_row + 1, stop + 1):
            if grid[i][j] == 2:
                c2 += 1
            else:
                break
        for i in range(grey_row + 1, stop + 1):
            if grid[i][j] == 4:
                c4 += 1
            else:
                break
        m2 = max(m2, c2)
        m4 = max(m4, c4)
    c = 2 if m2 >= m4 else 4
    return [[c, c], [c, c]]