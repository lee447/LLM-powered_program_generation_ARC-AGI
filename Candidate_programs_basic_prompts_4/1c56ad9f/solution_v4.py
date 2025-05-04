def solve(grid):
    h, w = len(grid), len(grid[0])
    def runs_line(line):
        runs = []
        j = 0
        while j < len(line):
            if line[j] != 0:
                c = line[j]
                start = j
                while j < len(line) and line[j] == c:
                    j += 1
                runs.append((start, j - start))
            else:
                j += 1
        return runs
    srows = [i for i in range(h) if len(runs_line(grid[i])) == 1 and runs_line(grid[i])[0][1] > 1]
    scols = []
    for x in range(w):
        col = [grid[y][x] for y in range(h)]
        if len(runs_line(col)) == 1 and runs_line(col)[0][1] > 1:
            scols.append(x)
    cell_rows = len(srows) - 1
    cell_cols = len(scols) - 1
    rotate = (cell_rows == cell_cols and cell_rows >= 2)
    connectors = (cell_rows == cell_cols and cell_rows <= 2)
    orig = grid
    res = [row[:] for row in grid]
    if connectors and srows:
        for y in (srows[0] + 1, srows[-1] - 1):
            if 0 <= y < h:
                newr = [0] * w
                for x in range(w):
                    if orig[y][x] != 0 and x - 1 >= 0:
                        newr[x - 1] = orig[y][x]
                res[y] = newr
    if rotate and srows:
        y = srows[len(srows) // 2]
        newr = [0] * w
        for x in range(w):
            if orig[y][x] != 0 and x + 1 < w:
                newr[x + 1] = orig[y][x]
        res[y] = newr
    return res