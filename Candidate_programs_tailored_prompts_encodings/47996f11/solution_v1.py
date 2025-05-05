def solve(grid):
    rows, cols = len(grid), len(grid[0])
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 6:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    h = max_r - min_r
    w = max_c - min_c
    new_min_r = max(min_r - 1, 0)
    new_max_r = min(max_r + 1, rows - 1)
    new_min_c = max(min_c - 1, 0)
    new_max_c = min(max_c + 1, cols - 1)
    out = [list(row) for row in grid]
    for i in range(new_min_r, new_max_r + 1):
        for j in range(new_min_c, new_max_c + 1):
            out[i][j] = 7
    if w > h:
        for i in range(new_min_r, new_max_r + 1):
            out[i][new_min_c] = 1
            out[i][new_max_c] = 1
    else:
        for j in range(new_min_c, new_max_c + 1):
            out[new_min_r][j] = 1
            out[new_max_r][j] = 1
    return out