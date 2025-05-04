def solve(grid):
    rows=len(grid)
    cols=len(grid[0])
    rmin, rmax = rows, -1
    cmin, cmax = cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    h = rmax - rmin + 1
    w = cmax - cmin + 1
    hh = (h + 1) // 2
    ww = (w + 1) // 2
    return [row[cmin:cmin+ww] for row in grid[rmin:rmin+hh]]