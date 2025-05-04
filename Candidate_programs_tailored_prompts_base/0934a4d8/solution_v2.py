def solve(grid):
    h, w = len(grid), len(grid[0])
    minr, maxr = h, -1
    minc, maxc = w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    H = maxr - minr + 1
    W = maxc - minc + 1
    start_col = minc - W
    return [row[start_col:minc] for row in grid[minr:maxr+1]]