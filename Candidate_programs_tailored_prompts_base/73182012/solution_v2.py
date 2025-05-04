def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    height = max_r - min_r + 1
    width = max_c - min_c + 1
    size = height if height > width else width
    row_extra = size - height
    top = row_extra // 2
    bottom = row_extra - top
    col_extra = size - width
    left = col_extra // 2
    right = col_extra - left
    r0 = min_r - top
    c0 = min_c - left
    half = size // 2
    return [[grid[i][j] for j in range(c0, c0 + half)] for i in range(r0, r0 + half)]