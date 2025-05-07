def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    minr, maxr = rows, -1
    minc, maxc = cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    h = maxr - minr + 1
    w = maxc - minc + 1
    rh = (h + 1) // 2
    rw = (w + 1) // 2
    return [row[minc:minc+rw] for row in grid[minr:minr+rh]]