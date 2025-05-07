def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    h = max_r - min_r + 1
    w = max_c - min_c + 1
    h2 = h // 2
    w2 = w // 2
    out = []
    for i in range(min_r, min_r + h2):
        out.append(grid[i][min_c:min_c + w2])
    return out